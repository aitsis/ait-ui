# __version.py
import os

def get_version():
    ## check if version.txt exists
    version_file_path = None
    if not os.path.isfile(os.path.join(os.path.dirname(__file__), "version.txt")):
        ## look up one directory
        if not os.path.isfile(os.path.join(os.path.dirname(os.path.dirname(__file__)), "version.txt")):
            raise FileNotFoundError("version.txt not found")
            exit(1)
        else:
            version_file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "version.txt")
    else:
        version_file_path = os.path.join(os.path.dirname(__file__), "version.txt")

    with open(version_file_path, "r") as f:
        version = f.read().strip()
    return version


__version__ = get_version()