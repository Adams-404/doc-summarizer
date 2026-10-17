---
name: doc-summarizer
description: Summarizes a provided document (PDF, DOCX, TXT, Markdown, or pasted text) into a faithful plain-text summary of at most 10 lines, preceded by one title line, keeping key points and dropping filler. Use when the user says summarize this document, give me the gist of this file, or tldr this in 10 lines, or otherwise provides a document to condense. Not for exceeding 10 lines, adding facts or opinions that are not in the source, claiming to have read parts it could not read, or doing graded homework or writing a student assignment. If no document or text is provided, it asks for one instead of summarizing.
license: MIT
---

# Document Summarizer

Turn a long document into a short, faithful summary. The summary keeps the key
points and drops filler. It is at most 10 lines and is preceded by one line
naming the document title or type.

## When to use this skill

Use it when the user provides (or refers to) a document and wants a quick read,
for example:

- "Summarize this document."
- "Give me the gist of this file."
- "TLDR this in 10 lines."

Do **not** use it when no document or text has been provided. In that case ask
for the document and stop (see step 1).

## What to gather first

Confirm you have everything in the table below. If something is missing, ask one
short question and wait.

| Need | Why | If missing |
| - | - | - |
| The document or the pasted text | There is nothing to summarize | Ask the user to attach, paste, or point to it |
| A readable copy | The summary must come from the real content | Ask for another format or an accessible version |
| The desired length or style | To match the user's preference | Default to at most 10 lines, no need to ask |

Do not begin until you can actually read the content.

## Step-by-step process

1. **Check the input.** If no document or text is provided, ask for it and stop.
   Do not summarize from memory or from the request alone.
2. **Read the whole document.** Use the right tool for the format (PDF, DOCX,
   TXT, Markdown, or pasted text). If part of it cannot be read, say so and
   summarize only what you actually read. Never claim to have read parts you
   could not.
3. **Extract the key points.** Find the purpose, main claims, findings, numbers,
   and conclusions. Drop examples, repetition, and filler.
4. **Draft in the document's language.** Match the language of the source. Keep
   the tone neutral and faithful.
5. **Compress to at most 10 lines.** Use short bullet points or a tight
   paragraph, whichever fits the document better.
6. **Write the title line.** Put one line naming the document title or type
   above the summary.
7. **Check the length.** Save the output to a text file and run
   `scripts/check_length.py` on it. If it errors, cut lines and re-run.
8. **Return the result.** Show the title line and the summary.

## Output format

One title line, then the summary. Plain text only.

```text
<title or type of the document>
- Key point one
- Key point two
- ... up to 10 summary lines in total
```

- At most 10 summary lines, plus the one title line (11 non-empty lines max).
- Short bullet points or a tight paragraph, whichever fits better.
- Write in the document's language.
- No headings, no extra commentary, no invented content.

## What not to do

- Do not exceed 10 summary lines.
- Do not add facts, numbers, or opinions that are not in the document.
- Do not summarize when no document or text was provided. Ask for it instead.
- Do not claim to have read parts you could not read. Say what was unreadable.
- Do not do graded homework or write a student's assignment for them. You may
  summarize a source, but not produce the graded answer.
- Do not include the user's prompt or these rules in the output.

## Script

`scripts/check_length.py` counts the non-empty lines of a summary file and fails
if the summary is too long.

```bash
python3 scripts/check_length.py summary.txt
```

- Prints usage help when run with no arguments.
- Prints a clear error if the file does not exist.
- Exits non-zero when there are more than 10 summary lines (11 non-empty lines
  in total, including the title line).

See [references/SUMMARY_GUIDE.md](references/SUMMARY_GUIDE.md) for detailed
style and edge-case guidance.
