"""Counts up the number of vowels contained in the string s.
Assume s is a string of lower case characters.
For example, if s = 'azcbobobegghakl', the program should print:
`Number of vowels: 5`
"""

count = 0
vowels = "aeiou"

for i in s:
    if i in vowels:
        count += 1
        
print("Number of values: " + str(count))