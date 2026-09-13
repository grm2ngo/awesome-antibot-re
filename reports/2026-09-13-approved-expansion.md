# Approved curation expansion — 2026-09-13

The maintainer approved all three proposed changes: historical methodological value, small substantive contributions, and Useful/Gold tiers. This update applies those rules to policy, config, contributor/readme guidance, validator and tests. It does not add resources or restore previously removed records.

## Rules

- Useful: 80–<85; Gold: 85–100. Scope and evidence remain ≥4/5 and all hard gates still apply. Tier is ranking, not runtime verification.
- Historical/undated snapshots need explicit historical_scope, snapshot_version, method_value and snapshot_artifact_urls within the inspected evidence. The studied version/artifact bounds the claim; current effectiveness cannot be inferred.
- Small scripts, VM handlers, traces, PoCs and original technical posts can qualify on mechanism/evidence. Complete products and polished presentation are not required.
- Current operational wording still requires the existing dated runtime evidence. Snapshot listings retain visible historical scope and limitations.

## Migration limits

Only policy_version changes in the existing resource records. Scores, sources, descriptions, review/test dates and acceptance state remain untouched. No additional independent source review is claimed by this schema migration. The validator checks structural snapshot evidence, while a human/independent reviewer still assesses whether the evidence actually supports the claim.

The three-day Codex council receives the approved rules in its saved prompt. Another scheduler described in repository settings has not been changed by this update.

## Validation

Boundary cases cover 80, 84.5, 85 and sub-threshold totals; reduced evidence still fails even with an accepted total. Snapshot tests require scope, method value and inspected evidence; misleading operational wording is rejected. Existing catalogue and Markdown links are checked too.

Gatekeeper policy_gatekeeper found a missing snapshot identifier requirement; fixed for all snapshot roles and covered by a negative test. Catalogue/Markdown validation, all 11 tests, and whitespace checks passed. No source was added or experimentally tested.
