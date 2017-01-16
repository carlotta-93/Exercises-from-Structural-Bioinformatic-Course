import Bio.PDB as PDB
parser = PDB.PDBParser(QUIET=True)

structure = parser.get_structure("2PTC", "2PTC.pdb")

