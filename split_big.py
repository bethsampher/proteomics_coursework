#!/usr/bin/python

"""
Reads in BIG.fa, extracts the amino acid
sequence and prints it in sections of max
500 residues with 100 residue overlap
"""

with open('/Users/bs15/ARU/PMS/BIG.fa') as fasta:
    lines = fasta.read().splitlines()

lines.pop(0) # remove fasta header
sequence = ''.join(lines)

for index in range(0, len(sequence), 400):
    print(sequence[index : index + 500] + '\n')
