import contextlib

def rosalind_input(problem, default):
    try:
        with contextlib.closing(open("rosalind_"+problem+'.txt')) as fp:
            return fp.readline().split('\n')[0]
    except Exception,r:
        return default
    
