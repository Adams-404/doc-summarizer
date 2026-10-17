# PROJECT

> What this project is, how it is built, and how to run it. Fill this from the
> repo itself during bootstrap. Names of env vars only — NEVER their values.

## What This Is
An Agent Skill named `doc-summarizer` that turns a document or pasted text into
a faithful plain-text summary of at most 10 lines plus one title line.
The repository root is the installable skill package.

## Stack
Markdown skill instructions and a dependency-free Python 3.9+ validation script.

## Architecture
`SKILL.md` defines the summarization workflow and output contract.
`references/SUMMARY_GUIDE.md` contains detailed guidance, while
`scripts/check_length.py` validates summary length.

## Folder Layout
The skill files are directly in the repository root; `references/` contains
supporting guidance and `scripts/` contains the length checker.

## Commands
| Action | Command |
|---|---|
| Install deps | None |
| Run (dev) | None |
| Build | None |
| Test | `python3 scripts/check_length.py <summary-file>` |
| Lint / typecheck | `agentskills validate .` |
| Run (prod) | None |
| Deploy | Copy the repository root into a skills directory |

## Environment Variables (names only, never values)
| Name | Purpose |
|---|---|
| | |

## Known Quirks
The package directory is named `doc-summarizer` when installed even though this
Git repository is named `summarization_skill`.

## External Services
<!-- APIs, third-party services, deployment targets. -->
