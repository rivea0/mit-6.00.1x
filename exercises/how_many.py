"""Returns the sum of the number of values associated with a dictionary."""

def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    total = 0
    
    for k in aDict:
        total += len(aDict[k])
  
    return total
