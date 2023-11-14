"""
File: main.py
Author: Austin Spadaro
Description: This is the main script for the Protein Structure Visualization tool. 
It takes a PDB (Protein Data Bank) file path as a command-line argument, parses the file 
to extract protein structure, and then visualizes it using 3D plotting. The script 
checks if the provided file path is valid and alerts the user if it's not.

Usage: Run this script from the command line and pass the path to a PDB file as an argument.
Example: python main.py <pdb_file_path>
"""

import os
import sys
from parse_pdb import parse_pdb
from visualize import visualize_structure
from setup_dependencies import install_dependencies

def main():
    # Check if we are installing dependencies
    if len(sys.argv) > 1 and sys.argv[1] == "--install-deps":
        install_dependencies()
        return

    if len(sys.argv) < 2:
        print("Usage: python main.py <pdb_file_path>")
        print("Please provide a PDB file path as a command-line argument.")
        sys.exit(1)

    pdb_file_path = sys.argv[1]
   
    if not os.path.isfile(pdb_file_path):
        print(f"Error: The file '{pdb_file_path}' does not exist. Please check the file path.")
        sys.exit(1)

    structure = parse_pdb(pdb_file_path)
    visualize_structure(structure)

if __name__ == "__main__":
    main()