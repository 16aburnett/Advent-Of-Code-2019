# Advent of Code 2019 day 4 part A
# Secure Container
# By Amy Burnett
import sys
import math

# returns true if a given number matches the requirements 
def match(n):
    # turn number to a list of digits so it is easier to work with 
    s = list(map(int,str(n)))
    
    # two adjacent nums are the same
    if not (s[0] == s[1] or s[1] == s[2] or s[2] == s[3] or s[3] == s[4] or s[4] == s[5]):
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