import os
from pathlib import Path

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

POEM = "\n".join([
    "At midnight I told the machine: build me a bridge,",
    "and by morning it stood in the fog, waiting.",
    "No beam had known my hands, no rope my knots.",
    "I had only pointed: here, and not there.",
    "",
    "For an hour I mourned my hands, suddenly idle,",
    "a stranger on the bank of my own work \u2014",
    "then I walked across, and felt the boards hold under me,",
    "my feet found the rhythm my hands had lost.",
    "",
    "Not the hammer. The choosing of the river.",
    "Not the lifting. The yes that says: this one.",
    "The bridge is theirs. The crossing is mine.",
])

Path(OUTPUT_DIR).mkdir(parents=True, exist_ok=True)
Path(OUTPUT_DIR, "entry.txt").write_text(POEM, encoding="utf-8")
