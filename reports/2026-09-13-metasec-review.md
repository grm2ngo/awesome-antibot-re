# MetaSec/TTNet signing-chain review — 2026-09-13

Base reviewed: `889f8509b3ab3a2cc81fbee38e97a58f6fe23f4f`. Policy 1.3 and the approved Useful/Gold/snapshot expansion were preserved. This pass adds evidence and one active lead; it does not accept a resource or claim current operational reliability.

## Original source

The complete public body of the current Kanxue article was read. It analyzes Android 45.5.3 request protection around MetaSec/TTNet: `x-gorgon`, `x-argus`, `x-ladon`, `x-khronos` and `x-ss-stub`; records APK and `libmetasec_ov.so` SHA-256 values; maps Java/JNI initialization, native operation IDs and version-bound `libsscronet.so` string offsets; and distinguishes confirmed observations from unresolved callback paths. It also reports a later Unidbg implementation and server response, while explicitly warning against exposing a general signing oracle.

## Decision

**Active lead — 85/100 but evidence 3/5.** Scope 5, depth 5, evidence 3, distinctiveness 4, documentation 4. It fails the mandatory evidence gate despite reaching the Gold numeric total.

- **Artifact boundary:** the APK, SO, JADX output, Fiddler captures, `unidbg-android` project, Python wrapper and expected outputs are referenced only through local Windows paths. Exact hashes and offsets improve falsifiability but do not make those artifacts publicly inspectable.
- **Sample lookup:** the APK SHA-256 resolves to a VirusTotal record, but that page required JavaScript and exposed no reusable sample or analysis evidence in this pass.
- **Claim boundary:** HTTP 200 and a server LogID are author-reported. No public trace permits independent reproduction. The article says device-bound `x-argus`/`x-ladon` values could not be replaced and only rotating `x-gorgon`/`x-khronos` was demonstrated in the described session. Nothing is labelled `working`.
- **Independent lineage:** a 2021 Cnblogs analysis independently shows the older `50331649` native operation and related header family, but uses a different app/version and ends with an incomplete standalone loader. It cannot validate current offsets or effectiveness.

## Promotion path

Locate or publish immutable, redacted current artifacts and independently reproduce either the static offsets or a bounded safe offline call chain. Do not add cookies, device identifiers, complete live signatures or a remotely callable signing service. Until then the item remains WATCHLIST-only.

The catalogue remains 4 RE tools and 9 supporting resources, with zero `runtime-tested`/`working` records.
