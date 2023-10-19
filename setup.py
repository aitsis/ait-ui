from setuptools import setup, find_packages
import shutil
## read version from file ../version.txt
import os
current_pkg_version = None

with open("version.txt", "r") as f:
    current_pkg_version = f.read().strip()
shutil.copyfile("version.txt", os.path.join(os.path.dirname(__file__), "ait-ui", "version.txt"))

setup(
    
    name="ait-ui",
    version = current_pkg_version, 
    description = "AIT UI",
    author = "AIT",
    packages = find_packages(),
    package_data= {
        "ait-ui": [ "static/*", "js/*", "version.txt" ]
    },
    exclude_package_data = {
        "ait-ui": [ "*.pyc", "requirements.txt", "README.md" ]
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
        
    
