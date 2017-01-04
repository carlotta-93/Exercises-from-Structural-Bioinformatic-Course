import Bio.PDB as PDB
import numpy as np

parser = PDB.PDBParser()

structure = parser.get_structure("Trypsin", "2PTC.pdb")

print structure

model = structure[0]
chain = model["E"]
residue = chain[16]
atom = residue["CA"]

# shortcut
atom = structure[0]["E"][16]["CA"]

# Loop over model
for model in structure:
    # Loop over chain
    for chain in model:
        # Loop over residues
        for residue in chain:
            # Loop over atoms
            for atom in residue:
                print atom

# Loop over model
for atom in structure.get_atoms():
    # Loop over all atoms in structure
    print atom
    # Get list of atoms in structure
    atom_list = list(structure.get_atoms())

# Atom name
atom.get_name()
# Temperature factor
atom.get_bfactor()
# Coordinates as array
atom.get_coord()
# Coordinates as Vector
atom.get_vector()
# Alternative location specifier
atom.get_altloc()

