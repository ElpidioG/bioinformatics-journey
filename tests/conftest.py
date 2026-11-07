"""Make the course module folders importable from tests/.

Example: a test here can do `from pattern_count import pattern_count`
for a script at ucsd-c1/module1/pattern_count.py.
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

for module_dir in sorted((ROOT / "ucsd-c1").glob("module*")):
    sys.path.insert(0, str(module_dir))
