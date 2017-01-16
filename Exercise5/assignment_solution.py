#!/usr/bin/env python
from __future__ import print_function
# Bio.PDB Assignment solution

import numpy as np
import Bio.PDB as PDB


def centroid(residue):
    """ Returns the centroid of the given residue."""
    coord_sum = np.zeros(3)
    for atom in residue:
        coord_sum += atom.get_coord()
    
    return coord_sum / len(residue)

# Download pdb
pdbl = PDB.PDBList()
pdbl.retrieve_pdb_file('2PTC', pdir='.')

# Load pdb file
parser = PDB.PDBParser()
struct = parser.get_structure("2PTC", "pdb2ptc.ent")

# Print the positions of CA and centroid of residue 20, chain E.
residue = struct[0]["E"][20]
print("Chain E residue %3s%-3d" % (residue.get_resname(), residue.get_id()[1]))
print("C-alpha: %s" % residue["CA"].get_coord())
print("centroid: %s" % centroid(residue))

# Print the positions of CA and centroid of residue 13, chain E.
residue = struct[0]["I"][13]
print("Chain I residue %3s%-3d" % (residue.get_resname(), residue.get_id()[1]))
print("C-alpha: %s" % residue["CA"].get_coord())
print("centroid: %s" % centroid(residue))
