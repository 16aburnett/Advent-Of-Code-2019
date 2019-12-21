# Advent of Code 2019 day 4 part B
# Secure Container
# By Amy Burnett
import sys
import math

# returns true if a given number matches the requirements 
def match(n):
    # turn number to a list of digits so it is easier to work with 
    s = list(map(int,str(n)))
    
    # find pair of adjacent same digits 
    # that arent a part of a larger set of adjacent same digits 
    i = 0
    j = 0
    if (s[0] == s[1] and not (s[1] == s[2])):
        i = 0
        j = 1
    elif (not (s[0] == s[1]) and (s[1] == s[2]) and not (s[2] == s[3])):
        i = 1
        j = 2
    elif (not (s[1] == s[2]) and (s[2] == s[3]) and not (s[3] == s[4])):
        i = 2
        j = 3
    elif (not (s[2] == s[3]) and (s[3] == s[4]) and not (s[4] == s[5])):
        i = 3
        j = 4
    elif (not (s[3] == s[4]) and (s[4] == s[5])):
        i = 4
        j = 5
    else:
        return False
    
    # increasing order
    b = list(s)
    b.sort()
    if s != b:
        return False
    return True 


# range input 
start = 245182
end = 790572

# loop through range 
num_matches = 0
for i in range(start,end):
    if match(i):
        print(i,"matches")
        num_matches += 1 

print("matches :", num_matches)