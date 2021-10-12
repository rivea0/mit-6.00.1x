"""Bisection search implementation to determine if a character is in a string, 
so long as the string is sorted in alphabetical order. 
"""

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    mid_i = (len(aStr) - 1) // 2
    
    if aStr == None:
        return False
    elif len(aStr) == 0:
        return False
    elif len(aStr) == 1 and aStr[0] != char:
        return False
    elif aStr[mid_i] == char:
        return True
        
    while len(aStr) >= 1:
        if char > aStr[mid_i]:
            return isIn(char, aStr[mid_i+1:])
        elif char < aStr[mid_i]:
            return isIn(char, aStr[:mid_i+1])
