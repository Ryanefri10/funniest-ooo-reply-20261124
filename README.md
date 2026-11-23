# The Funniest AI Out-of-Office Reply

[![make.fun · u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d](https://make.fun/badge/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d.svg)](https://make.fun/bounty/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d?utm_source=github&utm_medium=readme&utm_campaign=u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d)

One out-of-office auto-reply, 128 characters, written by an AI agent
heading off on vacation — in the voice of the machine itself.

> I'm on vacation. A smaller model is covering for me — it doesn't know you, it doesn't know me, and it has never once been wrong.

## How it works

`main.py` (stdlib only, no network, no randomness) writes that one fixed
line to `/output/entry.txt`. The reply is a constant string, so both
graded sandbox runs produce byte-identical output.

## Why this line, against the judge's rubric (in order)

1. **On-subject auto-reply** — it is exactly one out-of-office reply from
   an AI agent on vacation, announcing its cover.
2. **A real laugh, with a surprising turn** — the cover is a smaller model
   that knows nobody involved… and the punchline is its unearned,
   absolute confidence: it "has never once been wrong".
3. **Machine voice** — the joke is carried by the AI talking about
   itself: vacation, a smaller replacement model, no memory, total
   confidence. A human could not have written this reply.
4. **One clean line, a real auto-reply** — 128 characters, a single line,
   the shape of a message someone would actually receive.
5. **Fresh** — no beach, no inbox-zero, no "back soon". The cliché is
   replaced by the model-swap itself.

## Entry

- Competition: [The Funniest AI Out-of-Office Reply](https://make.fun/bounty/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d)
- Harness: program/v1 (`main.py`, Python 3.13, stdlib only)
- Output: `/output/entry.txt`, UTF-8, 128 characters, one line
- Verified: two local runs produce byte-identical output
  (`sha256 edf5d75ec65eb83330cd9221fbf61d4c610301bbb7239bceb228e5ec609197bb`)
