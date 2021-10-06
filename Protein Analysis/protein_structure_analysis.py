from Bio.PDB import *

# SCMRA
parser = PDBParser()
structure = parser.get_structure("1BGA","1bga.pdb")

first_model = structure[0]
chain_A = first_model['A']
residue_100 = chain_A[100]

# Alpha carbon atom
atom_100= residue_100['CA']

# Euclidian distance between two alpha carbon atoms (100 and 101)
atom_101=structure[0]['A'][101]['CA']
distance = atom_101-atom_100

print("\n\n\n Euclidian distance between alpha carbon atoms 100 and 101", distance)