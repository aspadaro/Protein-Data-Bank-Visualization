"""
File: visualize.py
Author: Austin Spadaro
Description: This script contains functions for visualizing protein structures, 
utilizing matplotlib for rendering 3D structural data.
"""

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def visualize_structure(structure):
    """
    Visualizes the 3D structure of a protein.

    This function takes a Biopython Structure object as input and uses matplotlib
    to create a 3D scatter plot of the protein's structure. Each atom in the protein
    is represented as a point in the 3D space.

    Parameters:
    structure (Bio.PDB.Structure.Structure): A Biopython Structure object representing
    the hierarchical structure of a protein.

    The function does not return anything but displays the 3D plot of the protein structure.
    """
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    for model in structure:
        for chain in model:
            for residue in chain:
                for atom in residue:
                    ax.scatter(atom.coord[0], atom.coord[1], atom.coord[2])
    plt.show()
