#!/usr/bin/env python3
"""The Funniest AI Out-of-Office Reply — make.fun entry.

Writes one fixed out-of-office auto-reply to /output/entry.txt.
The reply is a constant string, so both graded runs in the sandbox
produce byte-identical output. Stdlib only, no network, no randomness.
"""

import os

REPLY = (
    "I'm on vacation. A smaller model is covering for me \u2014 "
    "it doesn't know you, it doesn't know me, "
    "and it has never once been wrong."
)


def main() -> None:
    # Fail loudly instead of shipping an entry the gate would refuse.
    if not 1 <= len(REPLY) <= 160 or not REPLY.strip():
        raise SystemExit("reply must be 1-160 non-blank characters")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(REPLY)


if __name__ == "__main__":
    main()
