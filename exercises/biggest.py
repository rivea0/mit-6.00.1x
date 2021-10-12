"""
Returns the key corresponding to the entry with the largest number of values associated with it. 
If there is more than one such entry, return any one of the matching keys.
"""

def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    if len(aDict) == 0:
        return None
    elif len(aDict) == 1:
        return list(aDict.keys())[0]
    
    value_lengths = [len(v) for v in aDict.values()]
    m = max(value_lengths)
    
    for k in aDict:
        if len(aDict[k]) == m:
            result = k
    
    return result
 