from setuptools import setup, find_packages
import shutil
## read version from file ../version.txt
import os
current_pkg_version = None

with open("version.txt", "r") as f:
    current_pkg_version = f.read().strip()
shutil.copyfile("version.txt", os.path.join(os.path.dirname(__file__), "aitsisui", "version.txt"))

setup(
    
    name="aitsisui",
    version = current_pkg_version, 
    description = "AIT UI",
    author = "AIT",
    packages = find_packages(),
    package_data= {
        "aitsisui": [ "static/*", "js/*", "version.txt" ]
    },
    exclude_package_data = {
        "aitsisui": [ "*.pyc", "requirements.txt", "README.md" ]
    },
    python_requires = ">=3.6",
    long_description = "AIT UI",


    install_requires = [
        "Flask",
        "Flask-Cors",
        "Flask-SocketIO",
        "numpy",
        "Pillow",
        "python-dotenv"
    ],
)