"""Calculates the exponential base^exp by simply using successive multiplication."""

def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    result = 1
    
    for i in range(exp):
        result *= base
    
    return result
