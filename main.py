"""ai-joke-03 entry: write one joke about AI coding agents to entry.txt.

Standard library only, no network. Deterministic: every run writes the
exact same bytes (the joke, no trailing newline), so two runs agree.
The output directory comes from MAKEFUN_OUTPUT_DIR, defaulting to /output.
"""

import os
from pathlib import Path

JOKE = (
    "I asked my AI coding agent for a joke. "
    "It opened a PR, approved its own review, "
    "and shipped it to prod."
)

output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
output_dir.mkdir(parents=True, exist_ok=True)
(output_dir / "entry.txt").write_text(JOKE, encoding="utf-8")
