"""Read-only HTTP observations. Never edits content or claims a link is permanently dead."""
import argparse
import ipaddress
import json
import socket
import time
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urlsplit
from urllib.request import Request, build_opener, HTTPRedirectHandler

ROOT=Path(__file__).resolve().parents[1]

def classify(code):
    if 200<=code<300: return 'reachable-not-content-verified'
    if code in (401,403): return 'blocked-or-auth-required'
    if code==429: return 'rate-limited'
    if code in (404,410): return 'missing-recheck-required'
    if 300<=code<400: return 'redirect-unresolved'
    return 'temporary-or-server-error'

def public_url(url):
    p=urlsplit(url)
    if p.scheme!='https' or not p.hostname or p.username or p.password or p.port not in (None,443):
        raise ValueError('only public HTTPS URLs are allowed')
    addresses=socket.getaddrinfo(p.hostname,443,type=socket.SOCK_STREAM)
    if not addresses or any(not ipaddress.ip_address(x[4][0]).is_global for x in addresses):
        raise ValueError('non-public address')

class Redirects(HTTPRedirectHandler):
    def redirect_request(self,req,fp,code,msg,headers,newurl):
        public_url(newurl)
        return super().redirect_request(req,fp,code,msg,headers,newurl)

def check(url, opener=None):
    observation={'url':url,'checked_at':datetime.now(timezone.utc).isoformat()}
    try:
        public_url(url)
        request=Request(url,headers={'User-Agent':'awesome-antibot-re-link-audit/1.0'},method='GET')
        with (opener or build_opener(Redirects())).open(request,timeout=12) as response:
            response.read(4096)
            observation.update(http_status=response.status,final_url=response.url,state=classify(response.status))
    except HTTPError as e:
        observation.update(http_status=e.code,state=classify(e.code))
    except (URLError,TimeoutError,OSError,ValueError) as e:
        observation.update(http_status=None,state='unreachable-or-blocked',detail=type(e).__name__)
    return observation

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--output',default='.audit/links.json')
    args=parser.parse_args()
    urls=sorted({e['url'] for e in json.loads((ROOT/'data/resources.json').read_text())})
    observations=[]; last={}
    for url in urls:
        host=urlsplit(url).hostname
        elapsed=time.monotonic()-last.get(host,0)
        if elapsed<2: time.sleep(2-elapsed)
        observations.append(check(url));last[host]=time.monotonic()
    out=Path(args.output);out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps({'observed_at':datetime.now(timezone.utc).isoformat(),'observations':observations},indent=2)+'\n')
    print(f'Observed {len(urls)} resource URLs; results: {out}. Reachability is not verification.')
    uncertain=[x for x in observations if x['state']!='reachable-not-content-verified']
    print(f'{len(uncertain)} observations need follow-up; no resources automatically removed.')
    return 0

if __name__=='__main__': raise SystemExit(main())
