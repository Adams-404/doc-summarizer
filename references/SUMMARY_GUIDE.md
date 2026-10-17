# Summary Guide

Detailed guidance for the `doc-summarizer` skill. The core rules live in
`SKILL.md`. Read this file only when you need the extra detail.

## Contents

- The line budget
- Faithfulness rules
- Handling unreadable or partial content
- Choosing bullets or a paragraph
- Worked examples
- Edge cases

## The line budget

- The summary body is at most **10 non-empty lines**.
- The output starts with **one title line**, which is separate from the 10.
- The total is therefore at most **11 non-empty lines**.
- Blank lines do not count toward the limit.
- A "line" is a single line of text, so one bullet can wrap into several lines
  when displayed. Keep each bullet short enough to stay on one line in a plain
  text file.

Use `scripts/check_length.py` to confirm the count:

```bash
python3 scripts/check_length.py summary.txt
```

## Faithfulness rules

- Use only content that appears in the document.
- Do not add facts, figures, names, dates, or opinions of your own.
- Do not soften or strengthen the document's claims. If the source is
  uncertain, the summary stays uncertain.
- Keep important numbers, dates, and names exactly as written.
- If the document states a conclusion, keep it. If it does not, do not invent
  one.
- Preserve the original meaning even when you shorten the wording.

## Handling unreadable or partial content

- If the whole document cannot be read, tell the user and ask for another
  format or an accessible version. Do not guess the content.
- If only part can be read, summarize that part and state clearly what could
  not be read and why.
- Never claim to have read a page, section, or file that you could not open.

## Choosing bullets or a paragraph

- **Bullets** suit documents with several separate points, findings, or steps.
- **A tight paragraph** suits documents that argue one idea or tell one story.
- Either way, stay within 10 lines and keep the same level of detail.

## Worked examples

Input document (shortened):

> Global coffee prices rose 12 percent in 2024. The rise followed drought in
> Brazil and Vietnam, which together supply most arabica beans. Analysts expect
> prices to stay high through 2026 but see no shortage of supply. Retailers have
> begun passing the increase to consumers.

Output:

```text
Coffee market report
- Global coffee prices rose 12 percent in 2024.
- The rise followed drought in Brazil and Vietnam.
- Those two countries supply most arabica beans.
- Prices are expected to stay high through 2026.
- No supply shortage is expected.
- Retailers are passing the increase to consumers.
```

Note that every line comes from the document. Nothing new was added.

## Edge cases

- **No document provided.** Do not summarize. Ask the user for the document or
  the text, then stop.
- **Empty or near-empty file.** Tell the user there is no content to summarize.
- **Very short document.** A summary of fewer than 10 lines is fine. Never pad
  to reach 10.
- **Multiple documents.** If the user gives more than one, ask whether they
  want one combined summary or one summary per document.
- **Non-text files with images only.** Say that the text could not be
  extracted and ask for a text version.
- **Graded homework or assignments.** Summarize the source material if asked,
  but do not write the student's graded answer for them.
- **Language.** Write the summary in the same language as the document unless
  the user explicitly asks for another language.
