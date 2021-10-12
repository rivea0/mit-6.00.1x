"""Prints the longest substring of s in which the letters occur in alphabetical order. 
Assume s is a string of lower case characters.
For example, if s = 'azcbobobegghakl', the program should print:
`Longest substring in alphabetical order is: beggh`
"""

count = 0
new_string = ""

for i in range(1, len(s)):
    # If it is the first alphabetical pair, get the both characters
    if s[i-1] < s[i] and count == 0:
        new_string += s[i-1] + s[i]
        count += 1
    # If it is not the first alphabetical pair, 
    # continue adding the second character
    elif s[i-1] < s[i] and count != 0 or s[i-1] == s[i]:
        new_string += s[i]
    # If the pair is not alphabetical, separate them by space,
    # and either add the single character or continue adding 
    # the first character of the new pair
    else:
        if count == 0:
            new_string += s[i-1] + " "
        else:
            new_string += " " + s[i]
            count += 1
        
# Split the string of substrings
substrings = new_string.split(" ")

print("Longest substring in alphabetical order is: " + max(substrings, key=len))