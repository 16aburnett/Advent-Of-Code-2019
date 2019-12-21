import sys

file = open("input.txt")
sum = 0 
for line in file:
    n = int(line)
    n = n // 3 - 2
    sumx = 0 
    while n > 0:
        sumx += n
        n = n // 3 - 2
    sum += sumx 

print(sum)
