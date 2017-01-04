import Bio.PDB as PDB
import numpy as np
parser = PDB.PDBParser(QUIET=True)

structure = parser.get_structure("Trypsin", "2PTC.pdb")
# atom_list = list(structure.get_atoms())

# for atoms in structure[0]["E"][16]:
#     print atoms.get_vector()


def distance_residues(res1, res2):
    close_atoms = 0
    for atom1 in res1:
        for atom2 in res2:
            if atom1-atom2 < 3.5:
                close_atoms +=1
                if close_atoms>2:
                    return True
    return False

# list of store found residue pairs

close_pairs = []

print "Comparing chains"

# for residues1 in structure[0]["E"]:
#     for residues2 in structure[0]["I"]:
#         if distance_residues(residues1, residues2):
#             close_pairs.append((residues1, residues2))
# print close_pairs

# Phi/Psi angles for both proteins
for chain in structure[0]:
    poly = PDB.Polypeptide.Polypeptide(chain)
    print "Model %s Chain %s" % (str(structure[0]), str(chain)),
    print poly.get_phi_psi_list()

# Output Trypsine to a separate PDB file


class TripSelect(PDB.Select):

    def accept_chain(self, chain_selected):
        if chain_selected.id == 'E':
            return 1
        else:
            return 0

# Create PDBIO object
io = PDB.PDBIO()
# Set the structure
io.set_structure(structure)
# Save
select = TripSelect()
io.save('out.pdb', select)

# Output all atoms within a sphere of 10 arm of the center of trypsine to a separate PDB file

for residues in structure[0]["E"]:
    for atoms in residues:
        #coord = atoms.get_vector()
        distance = np.linalg.norm(atoms.coord)
    print distance






