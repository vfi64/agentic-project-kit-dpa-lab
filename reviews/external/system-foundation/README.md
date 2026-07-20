# External System-Foundation Review Package

Classification: `NON_AUTHORITATIVE_REVIEW_SNAPSHOT`

This directory is a transport and review projection for the falsifying architecture review of:

- `vfi64/agentic-governance-framework` PR #2 at `93f34672cbd153839efad9303d2e9bbf2938406a`;
- `vfi64/agentic-project-kit-dpa-lab` PR #7 at `80a6e72926cc0b8b72eb2978bff8a1d91c3821d0`;
- `vfi64/repository-operating-system` PR #2 at `9eee8139d23c3e03f3c7f2ee2fbf711f6e7ed896`;
- the deliberate non-change boundary for `vfi64/agentic-project-kit`.

The package does not grant this repository authority over AGF, ROS or the Kit. Every copied source remains attributable to its source repository and exact PR head.

## Mandatory pre-review gates

1. Parse `SOURCE_MANIFEST.json`.
2. Confirm that all nine declared changed source files exist at their package paths.
3. Recompute `content_sha256` and `git_blob_sha1` exactly as defined by `hash_contract`.
4. Confirm the declared changed-file sets:
   - AGF PR #2: five files;
   - DPA PR #7: one file;
   - ROS PR #2: three files.
5. Confirm that each file entry carries its source repository, PR number, exact PR head and original path.
6. Confirm that the snapshot and authority classifications are unambiguous.

Failure of any gate requires `REVIEW_PACKAGE_INVALID` with the exact discrepancy.

## Trust boundary

The public/readable DPA PR #7 may be compared independently against its live PR. A reviewer without credentials for private AGF and ROS can verify package-byte integrity but cannot independently authenticate their private-repository origin. Findings based on those files must therefore be marked as source-attributed rather than independently source-verified.

## Review scope

After successful package validation, perform the complete previously assigned falsifying four-repository architecture review. The Kit repository itself remains readable and may be inspected for compatibility and contradictions, but no Kit-side initiative change set exists.