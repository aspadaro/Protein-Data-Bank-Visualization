"""
File: parse_pdb.py
Author: Austin Spadaro
Description: A method for parsing a pdb file using the Bio.PDB.PDBParser method.
"""

from Bio.PDB import PDBParser

def parse_pdb(file_path):
    """
    Parses a PDB file and returns its structure.

    This function uses the Biopython PDBParser to parse a PDB (Protein Data Bank) file. 
    It extracts the structure of the protein described in the file. This structure 
    includes details about the different levels of the protein's organization, such as 
    its atoms, residues, and chains.

    Parameters:
    file_path (str): The file path of the PDB file to be parsed.

    Returns:
    Bio.PDB.Structure.Structure: A Biopython Structure object representing the 
    hierarchical structure of the protein as defined in the PDB file. This object 
    can be used for further analysis or visualization of the protein structure.
    """
    parser = PDBParser()
    structure = parser.get_structure("protein", file_path)
    return structure

