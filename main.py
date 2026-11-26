#!/usr/bin/env python3
"""Pigeon Pitch, One Line — entry for u-donrulezz-pigeon-pitch-one-line-af06c6cf.

Judge criteria (from competition.yaml, most important first):
  1. Delivers a one-line elevator pitch from a city pigeon to investors
     for its startup.
  2. Is the funnier of the two, with a real joke that lands rather than
     a mild pun or a straight description.
  3. Is original and surprising, with an idea or a twist the reader has
     not met before.
  4. Keeps the pigeon's voice and city life in view, so the pitch could
     only come from a pigeon.
  5. Fits one line in English within 200 characters, with every word
     earning its place.

Draft candidates (scored 1-5 per criterion, total /25):

  A. "We're Coo-ber: like Uber, but we already sit on your car and the
     fare is one fry, non-negotiable."
     C1=5 C2=3 C3=2 C4=4 C5=4  total=18
     Notes: on-subject and tight, but Coo-ber is the obvious first pun
     anyone writes; joke is mild, no real twist.

  B. "Invest in NestEgg: we turn park statues into premium condos -
     400 units, zero rent, infinite cooing, and the mayor can't evict
     what he can't catch."
     C1=4 C2=4 C3=4 C4=5 C5=3  total=20
     Notes: strong pigeon voice (statues, eviction), but the condo
     framing reads more like a bit than a startup pitch, and it runs
     long with filler ("premium", "infinite").

  C. "Our startup delivers your texts by pigeon in 3-5 business days,
     but unlike email we also shit on your ex's car en route - that's
     the premium tier."
     C1=5 C2=5 C3=4 C4=5 C5=4  total=23
     Notes: clear setup (slow pigeon mail) and a punchline only a
     pigeon can offer (the en-route favour). Real joke structure,
     not just a pun. WINNER.

  D. "We're Airbnb for ledges: 12,000 five-star perches downtown,
     checkout is when the hawk arrives, and we take payment in
     bread - crumbs, not crypto."
     C1=5 C2=4 C3=4 C4=5 C5=3  total=21
     Notes: funny details (hawk checkout), but "Airbnb for X" is a
     well-worn pitch template and the line sprawls.

Winner: C (23/25). Draft line below; revisions follow in later commits.

Revision 1: sharpen the investor framing and price the joke. The draft
opened with a flat "Our startup delivers..." — an elevator pitch to
investors should name the company and ask for the money up front
(criterion 1), so it now opens "Invest in PigeonPost:". The premium
tier also gets a price ("for $5 extra"), which turns the punchline
into an actual business model and lands the joke harder (criterion 2).
"Your texts" becomes "messages" (shorter, broader) and "we also shit"
loses the filler "also" (criterion 5).

Revision 2 (final): tighten every word (criterion 5) and sharpen the
deadpan. "We deliver messages in..." becomes "messages delivered
in..." — two words shorter, same meaning. The hyphen before the
premium tier becomes a full stop: "...en route. Premium tier." reads
as a flat sales closer and lets the punchline land before it. Final
line verified at 148 characters, one line, UTF-8.
"""

import os

LINE = (
    "Invest in PigeonPost: messages delivered in 3-5 business days "
    "\u2014 slower than email, but for $5 extra we shit on your ex's "
    "car en route. Premium tier."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
