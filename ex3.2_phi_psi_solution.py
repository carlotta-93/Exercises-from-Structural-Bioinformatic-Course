#!/usr/bin/env python3

import Bio.PDB as PDB

# Create parser object
p = PDB.PDBParser()
# Get structure
s = p.get_structure("2PTC", "2PTC.pdb")

def calc_phi_psi(structure):
    """
    Calculate phi,psi dihedral angles and return lists.
    Uses the polypeptide class. A polypeptide is a normal (index zero-based)
    list of residues that are covalently bonded to the next and previous
    list element. No waters or ions.
    """
    # Create a list of  polypeptide objects
    ppb = PDB.PPBuilder()
    pp_list = ppb.build_peptides(structure)

    # Get phi and psi angles
    phi_list = []
    psi_list = []
    # Iterate over polypeptide molecules
    for pp in pp_list:
        # Calculate phi and psi angles and unpack list and tuple
        for phi, psi in pp.get_phi_psi_list():
            # put them in the lists
            phi_list.append(phi)
            psi_list.append(psi)

    return phi_list, psi_list

phi_list, psi_list = calc_phi_psi(s)
print("Phi angles:")
print(phi_list)
print("Psi angles:")
print(psi_list)
