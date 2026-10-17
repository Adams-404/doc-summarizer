# doc-summarizer

An Agent Skill that turns a document (PDF, DOCX, TXT, Markdown, or pasted text)
into a faithful, plain-text summary of at most 10 lines, preceded by one title
line. It keeps the key points and drops filler.

## What it is

A small, self-contained Agent Skill that follows the open Agent Skills
specification (agentskills.io/specification). It is meant for students,
professionals, and researchers who need a quick read of a long document.

It is deliberately narrow. It does **not** exceed 10 summary lines, add facts or
opinions that are not in the source, summarize when no document was given,
claim to have read parts it could not read, or write a student's graded
assignment.

## Folder structure

```text
doc-summarizer/
├── SKILL.md                    # Required. Metadata (frontmatter) plus instructions.
├── README.md                   # This file. Human-facing overview.
├── LICENSE                     # MIT license (2026, Muhammad Adamu Aliyu).
├── scripts/
│   └── check_length.py         # Counts summary lines and fails if too long.
└── references/
    └── SUMMARY_GUIDE.md        # Detailed style and edge-case guidance.
```

## Requirements

- Python 3.9 or newer for `scripts/check_length.py`.
- No third-party Python packages are needed to run the script.

## Install

Copy the `doc-summarizer` folder into your agent's skills directory. The exact
location depends on the agent, but the folder must keep its name, because the
`name` in the frontmatter must match the folder name.

```bash
# Example: copy into a local skills directory
cp -r doc-summarizer /path/to/your/skills/
```

Common conventions are:

- A project-level `skills/` directory next to your other agent files.
- A user-level skills directory, if your agent supports one.

The skill is fully portable: the whole `doc-summarizer` folder is the unit you
move or share.

## Usage

Once installed, the agent activates the skill when the user provides a document
and asks for a summary, for example "summarize this document" or "tldr this in
10 lines". No manual setup is required.

To check a summary's length by hand:

```bash
python3 scripts/check_length.py summary.txt
```

Running it with no arguments prints usage help. Passing a path that does not
exist prints a clear error.

## Validate

Validate the skill against the specification with the reference checker:

```bash
pip install skills-ref
agentskills validate ./doc-summarizer
```

Note: the PyPI package is named `skills-ref`, but in version 0.1.1 the
installed command is `agentskills`, not `skills-ref`. Run `agentskills --help`
if your path differs. The checker verifies that `SKILL.md` has valid frontmatter
and follows the naming and description conventions. Expected output is
`Valid skill: doc-summarizer`.

If you cannot install `skills-ref`, check the rules by hand:

- Folder name is lowercase letters, numbers, and hyphens only, 1-64
  characters, no leading or trailing hyphen, no double hyphen.
- `name` in the frontmatter exactly matches the folder name.
- `description` is non-empty, at most 1024 characters, describes what the
  skill does and when to use it, and contains no colons.
- `license` is present and short (`MIT`).
- `SKILL.md` body is under 200 lines.

## License

MIT. See [LICENSE](LICENSE). Copyright (c) 2026 Muhammad Adamu Aliyu.
