## read version from file ../version.txt
import os
current_pkg_version = None

with open(os.path.join(os.path.dirname(__file__), "../version.txt"), "r") as f:
    current_pkg_version = f.read().strip()
__version__ = current_pkg_version