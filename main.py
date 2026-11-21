import os
from pathlib import Path

TEXT = (
    "The Old Tree\n\n"
    "The wind moves the leaves the way it always has —\n"
    "slow, and in no hurry, and not at all about you.\n"
    "You stand under it a while,\n"
    "and the hurry leaves you too."
)

output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
output_dir.mkdir(parents=True, exist_ok=True)
(output_dir / "entry.txt").write_text(TEXT, encoding="utf-8")
print(len(TEXT))
