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

## Repository structure

```text
summarization_skill/
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

Install the skill with the Skills CLI:

```bash
npx skills add Adams-404/doc-summarizer
```

To install it globally for your agents, use:

```bash
npx skills add Adams-404/doc-summarizer -g
```

The CLI discovers the root `SKILL.md` and installs the `doc-summarizer` skill
using the name declared in its frontmatter. To install manually, copy this
repository into your agent's skills directory:

```bash
cp -r . /path/to/your/skills/doc-summarizer
```

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
# Run this from a directory named doc-summarizer after installing the package.
agentskills validate /path/to/skills/doc-summarizer
```

Note: the PyPI package is named `skills-ref`, but in version 0.1.1 the
installed command is `agentskills`, not `skills-ref`. Run `agentskills --help`
if your path differs. The checker verifies that `SKILL.md` has valid frontmatter
and follows the naming and description conventions. Expected output is
`Valid skill: doc-summarizer`.

The validator requires the containing directory to be named `doc-summarizer`;
this checkout is named `summarization_skill`, so validate the copied install
directory rather than this repository root. If you cannot install `skills-ref`,
check the rules by hand:

- Folder name is lowercase letters, numbers, and hyphens only, 1-64
  characters, no leading or trailing hyphen, no double hyphen.
- `name` in the frontmatter exactly matches the folder name.
- `description` is non-empty, at most 1024 characters, describes what the
  skill does and when to use it, and contains no colons.
- `license` is present and short (`MIT`).
- `SKILL.md` body is under 200 lines.

## License

MIT. See [LICENSE](LICENSE). Copyright (c) 2026 Muhammad Adamu Aliyu.
