"""Prints the number of times the string 'bob' occurs in s.
Assume s is a string of lower case characters.
For example, if s = 'azcbobobegghakl', the program should print:
`Number of times bob occurs is: 2`
"""

count = 0

for i in range(len(s)):
    for j in range(len(s)):
        if s[i:j + 1] == "bob":
            count += 1
            
print("Number of times bob occurs is: " + str(count))