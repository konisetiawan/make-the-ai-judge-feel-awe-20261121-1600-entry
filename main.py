import os
from pathlib import Path

# The stars older than roads and names dwarf the brief human pause beneath them.
TEXT = """The Night Is Wide

The stars are in no hurry.
They were here before the road,
before the names on the stones.
You look up, and for a while
there is nothing to hurry for."""

output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
output_dir.mkdir(parents=True, exist_ok=True)
entry_path = output_dir / "entry.txt"
entry_path.write_text(TEXT, encoding="utf-8")
written_text = entry_path.read_text(encoding="utf-8")
assert 1 <= len(written_text) <= 280
assert written_text.strip()
print(len(written_text))
