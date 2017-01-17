import Bio.PDB as PDB
import numpy as np
import rotation_matrix as rm

parser = PDB.PDBParser(QUIET=True)

structure = parser.get_structure("2PTC", "2PTC.pdb")

chainI = structure[0]["I"]
chainE = structure[0]["E"]
atom_coord_chainI = []
atom_coord_chainE = []

for residues in chainI:
    if residues.has_id("CA"):
        for atoms in residues:
            atom_coord_chainI.append(atoms.get_coord())

for residues in chainE:
    if residues.has_id("CA"):
        for atoms in residues:
            atom_coord_chainE.append(atoms.get_coord())

# print atom_coord_chainI
# print atom_coord_chainE

coord_atoms_E = np.array(atom_coord_chainE)
coord_atoms_I = np.array(atom_coord_chainI)

# calculate the center of the two chains
center_I = coord_atoms_I.mean(0)
center_E = coord_atoms_E.mean(0)

# direction from chain E to chain I
direction_vector = center_I - center_E
direction_length = direction_vector / np.linalg.norm(direction_vector)

print "the direction of the vector from chain E to chain I is: " + str(direction_length)

# move the atoms in the chain of 20 ar in direction

for atoms in chainI.get_atoms():
    current_pos = atoms.get_coord()
    atoms.set_coord(current_pos + 20 * direction_length)

# Save pdb
io = PDB.PDBIO()
io.set_structure(structure)
io.save('2PTC_moved.pdb')

# rotation matrix
R = np.array([[0.01411312, 0.51660633, 0.85610672],
              [-0.30164955, 0.81850121, -0.48894101],
              [-0.95331441, -0.25134372, 0.16738567]])

# Update Inhibitor coordinates and find centre again
for residues in chainI:
    if residues.has_id("CA"):
        for atoms in residues:
            atom_coord_chainI.append(atoms.get_coord())

coords_I = np.array(atom_coord_chainI)
center_I_up = coords_I.mean(0)

for atom in chainI.get_atoms():
    pos = atom.get_coord()
    # move centre to origin, rotate, move back
    new_pos = R.dot(pos - center_I_up) + center_I_up
    atom.set_coord(new_pos)

# Save the structure
io.save('2PTC_moved_rotated.pdb')

# modify the b-factor
# Change b-factor of inhibitor and save structure
for i, atom in enumerate(chainI.get_atoms()):
    b = np.cos(i / 100. * 2 * np.pi) * 20 + 25
    atom.set_bfactor(b)

io.save('2PTC_bfactors.pdb')


