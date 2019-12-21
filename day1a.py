import sys

file = open("input.txt")
sum = 0 
for line in file:
    n = int(line)
    n = n // 3 - 2
    sum += n 

print(sum)
