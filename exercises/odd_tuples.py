"""
Takes a tuple as input, and returns a new tuple as output, 
where every other element of the input tuple is copied, starting with the first one.
"""

def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    newTup = ()
    
    for i in range(0, len(aTup), 2):
        newTup += (aTup[i],)
        
    return newTup