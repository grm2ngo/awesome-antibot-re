# DKAPTCHA evidence review — 2026-09-13

Base reviewed: `b28c1acecdeac6b50a1a5a4f7b1e141ddd257a0e`. This pass checked the original Kakao page, Kakao's dated tag index and an independent attendee recap. No resource was accepted and no operational claim was made.

## Findings

The original title identifies a Kakao Tech Meet talk about using map images and audio for abuse prevention. Kakao's own tag index dates the post to 2023-09-22. The publicly retrievable original body contains only the title/navigation; searches did not establish a public slide deck, transcript, repository, dataset or implementation artifact.

An independent event recap adds design detail: place-name/POI labels on map imagery, adversarial-looking white watermarks, evaluation against multiple OCR systems, and an audio route intended for visually impaired users. This is useful product-design context, but it contains no code, exact generation algorithm, evaluation data, versions or reproducible measurement procedure. It cannot satisfy the technical evidence gate for anti-bot/CAPTCHA RE.

## Decision

Remove DKAPTCHA from the active watchlist. The source is outside the 365-day current window and lacks the immutable artifact/method evidence needed even for a bounded snapshot under policy 1.3. A vague hope that slides may appear is not a concrete active evidence step.

The two reference edges remain as rejected-path evidence so future discovery does not re-add the title, attendee recap or Kakao brand reputation as if they were implementation proof. The catalogue remains 4 RE tools and 9 supporting resources, with zero `runtime-tested`/`working` records.
