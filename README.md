# Protein Structure Visualization Tool

## Description
This utility is designed for visualizing protein structures (also DNA/RNA structures) using data from PDB (Protein Data Bank) files. It allows users to input a PDB file and generates a 3D representation of the molecular structure.

## Getting Started

### Prerequisites
- Python 3.x
- pip (Python package manager)

### Installation
1. **Clone the Repository**
```
git clone https://github.com/aspadaro/Protein-Data-Bank-Visualization
cd Protein-Data-Bank-Visualization
```

2. **Install Dependencies**
Run the following command to install the necessary Python packages:
```
python main.py --install-deps
```

This command will trigger the installation of all required dependencies, such as Biopython and Matplotlib.

### Usage
To visualize a protein structure:
1. Ensure you have a PDB file available. You can download these from various online databases like RCSB Protein Data Bank.
2. Run the tool using the command:
```
python main.py path_to_your_pdb_file.pdb
```

Replace `path_to_your_pdb_file.pdb` with the actual path to the PDB file you want to visualize.

## Contributing
Contributions to this project are welcome. Please fork the repository and submit a pull request with your changes.

## License
MIT License

Copyright (c) 2023 Austin Spadaro

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

## Author
Austin Spadaro
