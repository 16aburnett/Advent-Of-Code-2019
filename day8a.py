# Advent of Code 2019 day 8 part A
# Space Image Format
# By Amy Burnett

rows = 6
cols = 25

# read input 
nums = list(map(int, list(input())))
print(nums)

# group into columns 
rows_ = []
while len(nums) != 0:
    rows_ += [nums[:cols]]
    nums = nums[cols:]
print(rows_)

# group into matrices 
matrices = []
while len(rows_) != 0:
    matrices += [rows_[:rows]]
    rows_ = rows_[rows:]
print(matrices)

# find matrix with fewest '0' digits 
fewest_zeros = 100000
fewest_zeros_matrix = matrices[0]
for matrix in matrices:
    num_zeros = 0
    for row in matrix:
        for col in row:
            if col == 0:
                num_zeros += 1 
    if num_zeros < fewest_zeros:
        fewest_zeros = num_zeros
        fewest_zeros_matrix = matrix 
print("fewest zeros matrix:\n",fewest_zeros_matrix)

# calc #of 1's times #of 2's 
num_ones = 0
num_twos = 0
for row in fewest_zeros_matrix:
    for col in row:
        if col == 1:
            num_ones += 1
        elif col == 2:
            num_twos += 1
print("1's ->",num_ones)
print("2's ->",num_twos)
print(num_ones * num_twos)