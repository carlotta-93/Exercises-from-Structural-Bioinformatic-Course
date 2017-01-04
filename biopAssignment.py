import Bio.PDB as PDB
parser = PDB.PDBParser(QUIET=True)

structure = parser.get_structure("2PTC", "2PTC.pdb")


def centroid(residue):

    """calculates the centroid of the residue given as parameter """
    # Bio.PDB.Vector to calculate center-of-mass
    center_of_mass = PDB.Vector(0, 0, 0)
    # counter for number of atoms
    n = 0
    for atoms in residue:
        center_of_mass += atoms.get_vector()
        n += 1
    # element-wise division
    center_of_mass /= n
    return center_of_mass

# print coordinates of the C-alpha atom of the amino acid with PDB residue number 20 in chain E
atom1 = structure[0]["E"][20]["CA"]
atom_coordinates = atom1.get_coord()
print 'atom1 coordinate: ' + str(atom_coordinates)

residue1 = structure[0]["E"][20]
# print the geometric center (centroid) of the above amino acid
print 'residue1 centroid: ' + str(centroid(residue1))

# 5: print coordinates of the C-alpha atom of the amino acid with PDB residue number 13 in chain I.
atom2 = structure[0]["I"][13]["CA"]
my_atom_coord = atom2.get_coord()
print 'atom2 coordinate: ' + str(my_atom_coord)

residue2 = structure[0]["I"][13]
# 6: print the geometric center (centroid) of the above amino acid
print 'residue2 centroid: ' + str(centroid(residue2))

