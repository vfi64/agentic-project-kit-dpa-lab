# Source Assumptions

Every item must be revalidated against the current `origin/main` before implementation.

| ID | Status | Assumption | Required validation |
|---|---|---|---|
| A-001 | NEEDS_MAIN_REPO_VALIDATION | The documentation registry can accept an optional `projection` block compatibly. | Run the real registry parser and validator. |
| A-002 | NEEDS_MAIN_REPO_VALIDATION | CURRENT_HANDOFF mixes current state and append-only historical prose. | Build a complete reader/writer graph. |
| A-003 | NEEDS_MAIN_REPO_VALIDATION | Existing handoff state is sufficient to render current state without new runtime authority. | Inspect state files and refresh helpers. |
| A-004 | NEEDS_MAIN_REPO_VALIDATION | Existing lifecycle findings can absorb projection drift without a parallel audit. | Inspect doc_lifecycle and suite integration. |
| A-005 | NEEDS_MAIN_REPO_VALIDATION | Existing refresh workflows can support Git-based cross-PR drift guards. | Inspect refresh artifacts and pre-merge checks. |
