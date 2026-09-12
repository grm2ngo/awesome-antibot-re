"""Validate editorial records and local Markdown links without network access."""
import json
import re
import sys
from datetime import date, timedelta
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]

def load(path):
    return json.loads(path.read_text(encoding='utf-8'))

def anchor(text):
    text = re.sub(r'\[([^\]]+)\]\([^)]*\)', r'\1', text)
    text = re.sub(r'<[^>]+>', '', text).lower()
    return re.sub(r'[^\w\- ]', '', text).replace(' ', '-')

def headings(text):
    found, counts = set(), {}
    for title in re.findall(r'^#{1,6}\s+(.+?)\s*#*$', text, re.M):
        name = anchor(title)
        n = counts.get(name, 0)
        counts[name] = n + 1
        found.add(name if n == 0 else f'{name}-{n}')
    found.update(re.findall(r'id=["\']([^"\']+)["\']', text))
    return found

def valid_url(value):
    try:
        u=urlsplit(value)
        return u.scheme == 'https' and bool(u.hostname) and not u.username and not u.password
    except (TypeError, ValueError):
        return False

def validate_resources(records, policy, today=None):
    today = today or date.today()
    errors, ids, urls = [], set(), set()
    required = ['id','title','url','category','kind','language','publisher_group','description',
                'why_include','limitations','verification','status','checked_at','review_due',
                'freshness','freshness_reason','date_basis','evidence_urls','score','score_rationale',
                'score_total','reviewer','policy_version','editorial_role','listing_file']
    for item in records:
        name=item.get('id','<missing>')
        missing=[k for k in required if not item.get(k)]
        if missing:
            errors.append(f'{name}: missing {missing}')
            continue
        if name in ids or item['url'].rstrip('/') in urls:
            errors.append(f'{name}: duplicate ID or canonical URL')
        ids.add(name); urls.add(item['url'].rstrip('/'))
        if not valid_url(item['url']) or any(not valid_url(u) for u in item['evidence_urls']):
            errors.append(f'{name}: invalid evidence/resource URL')
        if item['language'] not in policy['languages']:
            errors.append(f'{name}: unsupported language')
        if item['kind'] not in policy['review_days']:
            errors.append(f'{name}: unknown kind')
        if item['policy_version'] != policy['version']:
            errors.append(f'{name}: wrong policy version')
        if item['status'] != 'curated':
            errors.append(f'{name}: main ledger is for curated resources')
        editorial=policy['editorial']
        role=item['editorial_role']
        if role not in editorial['listings']:
            errors.append(f'{name}: unknown editorial role')
        elif item['listing_file'] != editorial['listings'][role]:
            errors.append(f'{name}: wrong listing for editorial role')
        if role in editorial['main_roles']:
            if any(not item.get(k) for k in editorial['core_required_fields']):
                errors.append(f'{name}: core RE needs target, method and artifact evidence')
            elif not isinstance(item['re_artifact_urls'],list) or any(
                not valid_url(u) or u not in item['evidence_urls'] for u in item['re_artifact_urls']
            ):
                errors.append(f'{name}: RE artifacts must be listed HTTPS evidence URLs')
        if role=='case-study' and any(not item.get(k) for k in editorial['case_required_fields']):
            errors.append(f'{name}: RE case needs sample and version scope')
        scores=item['score']; weights=policy['weights']
        if set(scores)!=set(weights) or any(type(v) not in (int,float) or not 0<=v<=5 for v in scores.values()):
            errors.append(f'{name}: invalid score dimensions')
        else:
            computed=sum(scores[k]*v/5 for k,v in weights.items())
            if abs(computed-item['score_total'])>0.001:
                errors.append(f'{name}: score total mismatch')
            if computed<policy['accept_score'] or scores['scope']<4 or scores['evidence']<4:
                errors.append(f'{name}: fails acceptance threshold')
        if set(item['score_rationale']) != set(weights) or any(not v.strip() for v in item['score_rationale'].values()):
            errors.append(f'{name}: incomplete score rationale')
        try:
            checked=date.fromisoformat(item['checked_at'])
            due=date.fromisoformat(item['review_due'])
            if checked>today or due<checked:
                errors.append(f'{name}: impossible review dates')
            period=policy['review_days'].get(item['kind'],0)
            if due>checked+timedelta(days=period):
                errors.append(f'{name}: review interval exceeds policy')
            dates=[]
            for key in ('published_at','substantively_updated_at'):
                if item.get(key):
                    d=date.fromisoformat(item[key]); dates.append(d)
                    if d>checked: errors.append(f'{name}: source date after review')
            if item.get('published_at') and item.get('substantively_updated_at') and item['substantively_updated_at']<item['published_at']:
                errors.append(f'{name}: update before publication')
            if item['freshness']=='recent' and (not dates or max(dates)<checked-timedelta(days=policy['fresh_window_days'])):
                errors.append(f'{name}: unsupported recent label')
        except (ValueError,TypeError):
            errors.append(f'{name}: invalid ISO date')
        if item['freshness'] not in policy['freshness_routes']:
            errors.append(f'{name}: unsupported freshness route')
        if item['freshness']=='snapshot':
            if item['kind']!='research' or role!='case-study':
                errors.append(f'{name}: snapshot is bounded research, not current tooling')
            if not item.get('published_at') and not any(
                re.search(r'/blob/[0-9a-f]{40}/',u) for u in item.get('re_artifact_urls',[])
            ):
                errors.append(f'{name}: undated snapshot needs an immutable artifact')
        if item['verification'] not in ('source-reviewed','code-reviewed','runtime-tested'):
            errors.append(f'{name}: unsupported verification level')
        if item['verification']=='code-reviewed':
            ev=item.get('code_review') or {}
            if not all(ev.get(k) for k in ('url','commit_or_blob','inspection_note')):
                errors.append(f'{name}: code review needs immutable evidence')
        if item['verification']=='runtime-tested':
            test=item.get('runtime_test') or {}
            if not all(test.get(k) for k in ('version','environment','procedure','expected','actual','tested_at','evidence_url')):
                errors.append(f'{name}: runtime-tested without test evidence')
            else:
                try:
                    tested=date.fromisoformat(test['tested_at'])
                    if tested>today or tested<today-timedelta(days=30):
                        errors.append(f'{name}: runtime evidence outside 30-day window')
                except ValueError:
                    errors.append(f'{name}: invalid tested_at')
        elif re.search(r'\b(working|undetectable|guaranteed)\b',item['description'],re.I):
            errors.append(f'{name}: unsupported operational wording')
    return errors

def validate_markdown(root):
    errors=[]
    for path in root.rglob('*.md'):
        if '.git' in path.parts: continue
        text=path.read_text(encoding='utf-8')
        # The preserved old catalogue has obsolete historical anchors; no new links are added there.
        if path.relative_to(root).as_posix()=='catalog/LEGACY.md': continue
        if len(re.findall(r'^```',text,re.M))%2: errors.append(f'{path.name}: unclosed fence')
        for target in re.findall(r'\[[^\]]*\]\(([^\s)]+)(?:\s+"[^"]*")?\)',text):
            if urlsplit(target).scheme or target.startswith('//'): continue
            parsed=urlsplit(target)
            file=(path.parent/unquote(parsed.path)).resolve() if parsed.path else path
            if not file.is_relative_to(root):
                errors.append(f'{path.name}: link escapes repository: {target}')
            elif not file.exists():
                errors.append(f'{path.name}: missing local link: {target}')
            elif parsed.fragment and file.suffix=='.md' and unquote(parsed.fragment) not in headings(file.read_text()):
                errors.append(f'{path.name}: missing anchor: {target}')
    return errors

def validate(root=ROOT):
    p=load(root/'config/curation.json'); records=load(root/'data/resources.json')
    errors=validate_resources(records,p)+validate_markdown(root)
    if sum(p['weights'].values()) !=100: errors.append('weights must sum to 100')
    if len(p['languages'])!=len(set(p['languages'])): errors.append('duplicate language lanes')
    lanes=load(root/'config/languages.json')
    if {x['language'] for x in lanes}!=set(p['languages']): errors.append('language registry mismatch')
    listings={name:(root/name).read_text() for name in set(p['editorial']['listings'].values())}
    for e in records:
        listing=e.get('listing_file')
        if f']({e["url"]})' not in listings.get(listing,''):
            errors.append(f'{e["id"]}: missing from designated listing')
        if e.get('editorial_role')=='supporting' and f']({e["url"]})' in listings['README.md']:
            errors.append(f'{e["id"]}: supporting resource must not substitute for main RE entries')
    source_ids=set()
    for s in load(root/'data/sources.json'):
        if s['id'] in source_ids: errors.append('duplicate source ID')
        source_ids.add(s['id'])
        if not valid_url(s['url']) or not s['selection_rule'] or not s['discovery_only']: errors.append(f'{s["id"]}: invalid source seed')
        if s['status'] not in ('pending','blocked','directory-checked','content-checked'): errors.append(f'{s["id"]}: invalid status')
        if s['status']=='pending' and s['checked_at'] is not None: errors.append(f'{s["id"]}: pending seed cannot claim checked date')
    for r in load(root/'data/references.json'):
        if not valid_url(r['parent_url']) or not valid_url(r['child_url']) or r['parent_url']==r['child_url']: errors.append('invalid reference edge')
        if not 1<=r['depth']<=p['discovery']['max_depth']: errors.append('reference depth exceeds budget')
    return errors

if __name__=='__main__':
    errors=validate()
    for error in errors: print(error,file=sys.stderr)
    if errors: sys.exit(1)
    print('PASS: catalogue evidence, scores, dates, registries and local Markdown links.')
