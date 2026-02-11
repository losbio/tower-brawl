# Minimal pythonrc for pygbag web bootstrap.
# Keep this file intentionally small to avoid startup failures.

import sys

# Ensure current working directory is on path
if "" not in sys.path:
    sys.path.insert(0, "")
