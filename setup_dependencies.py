"""
File: setup_dependencies.py
Author: Austin Spadaro
Description: 
This script is designed to automate the installation of required dependencies 
for the Protein Structure Visualization tool. It defines a function to install 
each dependency using pip, Python's package manager. The script can be run independently 
or called from another script (like main.py) to ensure all necessary packages are 
installed before running the main application.

Usage:
To run this script directly from the command line:
    python setup_dependencies.py
"""

import subprocess
import sys

def install_dependencies():
    """
    Installs required dependencies for this project.
    """
    dependencies = ['biopython', 'matplotlib', 'mpl_toolkits']
    for dep in dependencies:
        subprocess.check_call([sys.executable, "-m", "pip", "install", dep])

if __name__ == "__main__":
    install_dependencies()