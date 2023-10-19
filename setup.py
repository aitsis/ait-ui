from setuptools import setup, find_packages
import shutil
## read version from file ../version.txt
import os
current_pkg_version = None

with open("version.txt", "r") as f:
    current_pkg_version = f.read().strip()
shutil.copyfile("version.txt", os.path.join(os.path.dirname(__file__), "aitui", "version.txt"))

setup(
    
    name="aitui",
    version = current_pkg_version, 
    description = "AIT UI",
    author = "AIT",
    packages = find_packages(),
    package_data= {
        "aitui": [ "static/*", "js/*", "version.txt" ]
    },
    exclude_package_data = {
        "aitui": [ "*.pyc", "requirements.txt", "README.md" ]
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
        
    
