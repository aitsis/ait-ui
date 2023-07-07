from setuptools import setup, find_packages
import shutil
## read version from file ../version.txt
import os
current_pkg_version = None
version_file_path = os.path.join(os.path.dirname(__file__), "version.txt")

if os.path.isfile(version_file_path):
    with open(version_file_path, "r") as f:
        current_pkg_version = f.read().strip()
    shutil.copyfile(version_file_path, os.path.join(os.path.dirname(__file__), "ait_ui", "version.txt"))
else:
    raise FileNotFoundError("version.txt not found")
    exit(1)

setup(
    
    name="ait_ui",
    version = current_pkg_version, 
    description = "AIT UI",
    author = "AIT",
    packages = find_packages(),
    package_data= {
        "ait_ui": [ "static/*", "version.txt" ]
    },
    exclude_package_data = {
        "ait_ui": [ "*.pyc", "requirements.txt", "README.md" ]
    },
    python_requires = ">=3.6",


    install_requires = [
        "Flask",
        "Flask-Cors",
        "Flask-SocketIO",
        "numpy",
        "Pillow",
        "python-dotenv"
    ],
)
        
    
#test