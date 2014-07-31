from rosalind_input import *

def dna(instr):
    res={}
    for i in range(len(instr)):
        if instr[i] not in res:
            res[instr[i]] = 0
        res[instr[i]] = res[instr[i]] + 1
    return res

r=dna(rosalind_input("dna","AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"))
print str(r['A'])+' '+str(r['C'])+' '+str(r['G'])+' '+str(r['T'])
