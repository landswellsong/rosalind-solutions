from rosalind_input import *

def rna(instr):
    res=instr
    for i in range(len(instr)):
        if res[i]=='T':
            res= res[:i]+'U'+res[i+1:]
    return res

print rna(rosalind_input("rna","GATGGAACTTGACTACGTAAATT"))

