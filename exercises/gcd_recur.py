"""Recursive implementation to find the greatest common divisor of two positive integers.
Implements Euclid's algorithm to find gcd recursively.
(https://en.wikipedia.org/wiki/Euclidean_algorithm#Worked_example)
"""

def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    if a == 0:
        return b
    if b == 0:
        return a
    
    return gcdRecur(b, a % b)
