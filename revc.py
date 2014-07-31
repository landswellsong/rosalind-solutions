from rosalind_input import *

def revc(instr):
    return ''.join(map(lambda x: {'A':'T',
                                  'C':'G',
                                  'G':'C',
                                  'T':'A'}[x], list(instr[::-1])))

print revc(rosalind_input("revc","AAAACCCGGT"))

