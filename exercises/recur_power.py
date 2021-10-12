"""Computes base^exp with recursion."""

def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    if exp == 1:
        return base
    if exp == 0:
        return 1
    
    return base * recurPower(base, exp - 1)
