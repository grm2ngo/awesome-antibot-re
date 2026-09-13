# Latest-only catalogue reset — 2026-09-13

Base reviewed: `a31b76d84cef713e82dda8ad25e9e1bc13df0df7`. Publication does not renew any source date.

## Decision

Applied the owner's latest-only rule across the ledger and listings.

- Removed 10 version-bounded or old case studies from the current tree.
- Kept 13 records: 4 current RE tools and 9 current supporting references.
- Removed the archive/migration catalogue files, superseded reports and old review files.
- Removed 15 reference edges belonging only to removed records; 21 useful discovery edges remain.
- Replaced the broad unresolved queue with six plausibly active leads having concrete evidence steps.
- No record is labelled `runtime-tested` or `working`.

The removals do not assert that older work lacks educational value. It simply does not satisfy this repository's current-only product decision. Git history preserves the prior evidence and rationale.

## Current acceptance boundary

A source must be within 365 days or a living project with current primary documentation/status evidence. Core records still need target, method and inspected artifact; support records need a concrete RE operation. PoW and working claims retain their stronger reproducibility requirements.

No new candidate was accepted in this cleanup. Source registry observations and checked dates were not rewritten.

Current-status verification on 2026-09-13 covered the 12 retained GitHub projects through repository metadata; none was archived or disabled. Their primary documentation had already been inspected at the ledger's recorded dates, and the status URLs are now evidence fields. This check establishes current project status only, not runtime operation or content quality. The current Chrome DevTools Protocol page was also read directly: it exposes tip-of-tree and stable protocol routes and warns that tip-of-tree can break without compatibility guarantees.

## Validation

Run before publication:

- `python3 scripts/validate.py`
- `python3 -m unittest discover -s tests -v`
- whitespace/diff inspection

## Workflow health

The latest observed run before this change was [push run 34716143317](https://github.com/grm2ngo/awesome-antibot-re/actions/runs/34716143317), created 2026-09-12 20:07:10 UTC. It concluded failure. This catalogue does not call the schedule healthy unless a run reaches and passes actual validation steps.

## Next queue

Kakao DKAPTCHA transcript/slides; exact current Japanese code articles; Kanxue signing artifacts; Vietnamese implementation RE; then current DataDome, Kasada, PerimeterX/HUMAN and hCaptcha leads with public artifacts. GitHub Following remains unused until the connector returns the real public list.
