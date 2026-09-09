# Curation guide

Use this guide when adding, revising, or retiring resources. The list values technical learning over size, popularity, or advertised success rates.

## Selection

Eligible resources are public code, original articles, papers, talks, and datasets relevant to browser anti-bot reverse engineering or detection. Exclude paid solving services, API storefronts, account markets, gated content, and SEO summaries without original technical work. Commercial authors may contribute useful public research; judge the actual resource.

Score each dimension from 0 (absent), through 1 (partial), to 2 (strong):

| Dimension | Evidence for 2 points |
| --- | --- |
| Scope fit | Directly teaches a listed research area |
| Technical depth | Explains mechanisms with code, traces, experiments, or detailed analysis |
| Verifiable evidence | Original material supports the proposed description |
| Distinctive value | Adds a method, dataset, or perspective beyond existing entries |
| Documentation | Accessible explanation with enough context to use or study it |

Include candidates scoring at least 8/10, with nonzero scope fit and evidence. Stars are not evidence. A fork needs a substantive, described contribution. There is no addition quota.

## Review process

1. Read the current list and synchronize the checkout, preserving unrelated work.
2. Convene a repository/source scout, an article/paper/talk scout, and a skeptical editor as subagents. Scouts inspect original materials and exchange findings; the editor challenges relevance, duplication, and unsupported claims. The parent resolves disagreements using evidence.
3. Record candidate URL, inspected material, five scores, date provenance, and inclusion/rejection reason in a local run log. Read code or the original article before accepting an entry; search snippets alone are insufficient.
4. Write one concise English description explaining what the reader can study. Use a verified activity or publication date; record verification dates separately. Avoid implying present-day effectiveness from a recent push.
5. Check changed URLs, local anchors, unintended duplicates, and the complete diff. Cross-references are allowed. Publish only meaningful, verified changes.

## Maintenance

Daily discovery is scheduled for 09:00 Asia/Saigon through the maintainer's Codex task. Each run checks a rotating sample of existing entries; a full audit is due quarterly. Scheduling is external to this repository.

Archived or old work may remain when its methodology is useful; label it Historical and describe limitations. For inaccessible resources, check redirects, repository moves, and author archives before removal. A single timeout, 403, or 429 does not establish a dead link. Remove sources that become unavailable after confirmation, duplicate other entries without added value, or cease meeting the scope.

Keep publication claims separate from successful pushes. When credentials or branch protections prevent publication, preserve the proposed changes and report the blocker. Never force-push or create empty commits merely to update dates.
