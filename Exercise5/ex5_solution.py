import numpy as np
import Bio.PDB as PDB


# Download pdb
pdbl = PDB.PDBList()
pdbl.retrieve_pdb_file('2PTC', pdir='.')

# Load pdb file
parser = PDB.PDBParser()
structure = parser.get_structure("2PTC", "pdb2ptc.ent")

# Easy access to the two chains
chainE = structure[0]['E']
chainI = structure[0]['I']

# Get coordinate lists (python list of numpy arrays, xyz.)
# filtered to only include atoms from residues with a CA atom
coords_list_E = [a.get_coord() for a in chainE.get_atoms() if a.get_parent().has_id('CA')]
coords_list_I = [a.get_coord() for a in chainI.get_atoms() if a.get_parent().has_id('CA')]

# Alternative solution to extracting atom coordinates
coords_list_E_alternative_solution = []
for res in chainE:
    if res.has_id('CA'):
        for atom in res:
            coords_list_E_alternative_solution.append(atom.get_coord())

# Turn lists into numpy arrays, shape = (n_atoms, 3)
coordsE = np.array(coords_list_E)
coordsI = np.array(coords_list_I)

# Find centre
cE = coordsE.mean(0)
cI = coordsI.mean(0)

# Get vector from enzyme to inhibitor
diff = cI - cE

# Normalize vector (make it unit length)
direction = diff / np.linalg.norm(diff)

print "The direction of chain I from chain E is %s" % direction

# Move all atoms in the I chain
i = 0
for atom in chainI.get_atoms():
    pos = atom.get_coord()
    atom.set_coord(pos + direction * 20)

# Save pdb
io = PDB.PDBIO()

io.set_structure(structure)
io.save('2PTC_split.pdb')


# Rotate inhibitor

# Rotation matrix that rotates 90 degrees counterclockwise around
# the axis between enzyme and inhibitor. The rotation is around the origin.

R = np.array([[ 0.01411312,  0.51660633,  0.85610672],
              [-0.30164955,  0.81850121, -0.48894101],
              [-0.95331441, -0.25134372,  0.16738567]])


# Update Inhibitor coordinates and find centre again
coords_list_I = [a.get_coord() for a in chainI.get_atoms() if a.get_parent().has_id('CA')]
coordsI = np.array(coords_list_I)
cI = coordsI.mean(0)

# Rotate each atom around the centre of the inhibitor according to the rotation matrix R
for atom in chainI.get_atoms():
    pos = atom.get_coord()
    # move centre to origin, rotate, move back
    new_pos = R.dot(pos - cI) + cI
    atom.set_coord(new_pos)

io.save('2PTC_split_rotate.pdb')


# Change b-factor of inhibitor and save structure
for i, atom in enumerate(chainI.get_atoms()):
    b = np.cos(i / 100. * 2 * np.pi) * 20 + 25
    atom.set_bfactor(b)

io.save('2PTC_altered_b.pdb')
