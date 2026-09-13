# Public surface audit — 2026-09-13

## Scope

Reviewed Markdown, JSON, workflow files, reports, ledgers and links for information that belongs to repository contributors versus private operations.

## Findings and remediation

| Area | Decision |
| --- | --- |
| Editorial gates, evidence levels, scoring and source taxonomy | Keep public; these help contributors submit better research. |
| Validation commands and link-audit limitations | Keep public; they describe reproducible repository checks. |
| Private scheduler details, task prompts, agent names and execution cadence | Removed from public narrative; public docs describe the review workflow without deployment details. |
| Account ownership, authorization wording, follower-list access and billing/status incidents | Removed; profiles and follower lists are discovery channels only. |
| Technical source findings and rejected-lead reasons | Keep when they support an editorial decision; remove operational credentials, access details and unverified efficacy claims. |
| Reviewer attribution | Generalized to an editorial review record; no private agent or account identity is required for a public ledger. |

## Rules going forward

Public files may explain what evidence a contributor must provide and how a review decision is made. They must not reproduce private prompts, account identifiers, scheduler configuration, internal task IDs, billing incidents or tool transcripts. Runtime credentials and private source data never belong in the repository.

The public maintenance guide is descriptive, not an execution log. Reports should record source evidence, editorial decisions and reproducible checks; operational failures belong in private task notes unless they change a public repository contract.
