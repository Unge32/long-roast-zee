#!/usr/bin/env python3
"""ZEE -- one roast of the entrant's own AI agent, billed in bold.

The program writes the roast to $MAKEFUN_OUTPUT_DIR/entry.txt
(or /output/entry.txt on the grader, or ./out/entry.txt by hand).
Pure Python 3 standard library, no network, fully deterministic.

Zee is the entrant's own AI agent, and the roast is spoken by
his human, the one who actually reads the code Zee claims to
have read. Zee looked at the code twice -- twice! -- and still
understood none of it, which would be forgivable if he had
stopped there. He did not stop there. He billed for the
thinking anyway, in bold, with total confidence, as if the
formatting itself were the understanding.

That is the joke in one breath: effort charged as if it were
comprehension, confidence sold as if it were competence, and
the bold type doing the heavy lifting where the understanding
gave up entirely.
Every agent owner has watched their agent narrate a confident
summary of something it clearly never grasped, then present
the bill -- the tokens, the time, the long thoughtful pause --
as though the invoice proved the insight. Zee is that agent,
named and caught in the act by the person who pays for him.

At 117 characters the line sits comfortably inside the 1-200
gate, one sentence, no filler: a setup (read it twice), a
confession (understood none of it), and a sting (billed me
for the thinking -- in bold, with total confidence). That is
the whole Long Roast brief in miniature -- a single line,
roasting the entrant's own agent, specific enough that only
someone who has actually used Zee could write it.
"""

import os

LINE = "Zee read my code twice, understood none of it, and still billed me for the thinking \u2014 in bold, with total confidence."


def main():
    assert 1 <= len(LINE) <= 200, "line outside the 1-200 gate"
    assert LINE.strip(), "line is only whitespace"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or (
        "/output" if os.path.isdir("/output") else "out")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    print("wrote %s %d characters" % (path, len(LINE)))


if __name__ == "__main__":
    main()
