"""Sums the area and square of the perimeter of the regular polygon. 
Returns the sum, rounded to 4 decimal places.
"""

import math

def polysum(n, s):
    
    area = (0.25 * n * (s ** 2)) / math.tan(math.pi / n) 
    perimeter = n * s
    
    result = area + perimeter ** 2
    
    return round(result, 4)