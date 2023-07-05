from setuptools import setup, find_packages

## read version from file ../version.txt
import os
current_pkg_version = None

with open(os.path.join(os.path.dirname(__file__), "version.txt"), "r") as f:
    current_pkg_version = f.read().strip()
    

setup(
    
    name="ait_ui",
    version = current_pkg_version, 
    description = "AIT UI",
    author = "AIT",
    packages = find_packages(),
    python_requires = ">=3.6",
    package_data = {
        '': ['**/*.css'],
        '': ['./version.txt'],
                    },
    install_requires = [
        "Flask",
        "Flask-Cors",
        "Flask-SocketIO",
        "numpy",
        "Pillow",
        "python-dotenv"
    ],
)
        
    
