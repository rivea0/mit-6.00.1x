"""Iterative implementation to find the greatest common divisor of two positive integers."""

def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    test = min(a, b)
    
    while test >= 1:
        if a % test == 0 and b % test == 0:
            return test
        elif test == 1:
            return test
        test -= 1
    
    return test

