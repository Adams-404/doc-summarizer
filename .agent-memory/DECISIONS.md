# DECISIONS

> Append-only. Record a decision at the moment it is made, not later.
> Every entry needs a REASON and the alternatives that were rejected.
> A decision with no reason is just a preference and will be re-litigated.

## D-001
- Date: YYYY-MM-DD
- Decision:
- Reason:
- Alternatives rejected:
  -  — why rejected:
- Affects:

<!--
### Format
Copy the block above, bump the number, append to the BOTTOM of this file.
Do not delete or rewrite old entries. Supersede instead:

## D-014
- Date: YYYY-MM-DD
- Decision: Switched auth from X to Y
- Supersedes: D-007
- Reason:
- Alternatives rejected:
-->
## 1. Flatten the installable skill package into the Git repository root

- **Decision:** Keep the existing `doc-summarizer` skill name in `SKILL.md`, but
  place the package files directly at the repository root.
- **Reason:** The user explicitly requested that projects not be nested below
  the root directory; the frontmatter name remains stable for installation.
- **Alternatives rejected:** Keeping a nested `doc-summarizer/` directory would
  preserve the old layout but would not satisfy the requested root placement.
