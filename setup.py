from setuptools import setup, find_packages

setup(
    
    name="ait_ui",
    version = "0.1.0", 
    description = "AIT UI",
    author = "AIT",
    package_dir = {"":"src"},
    packages = find_packages(where="src"),
    python_requires = ">=3.6",
    package_data = {
        '': ['**/*.css'],
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
        
    
