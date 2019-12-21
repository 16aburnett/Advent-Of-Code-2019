# Advent of Code 2019 day 8 part B
# Space Image Format
# By Amy Burnett

# prints a matrix in a clean way 
def pmatrix(m):
    for row in m:
        for col in row:
            if col == 0:
                print(' ',end="") # black pixels are blank 
            else:
                print(col,end="")
        print()


rows = 6
cols = 25

# read input 
nums = list(map(int, list(input())))

# group into columns 
rows_ = []
while len(nums) != 0:
    rows_ += [nums[:cols]]
    nums = nums[cols:]

# group into matrices 
matrices = []
while len(rows_) != 0:
    matrices += [rows_[:rows]]
    rows_ = rows_[rows:]

for matrix in matrices:
    print()
    pmatrix(matrix)

# find top layer
# start at the top and grab the first 0 or 1 
# if a 2 is encountered, 
# then move on to the next layer for that pos
final_matrix = [[0 for j in range(cols)] for i in range(rows)] 

for i in range(rows):
    for j in range(cols):
        for k in range(len(matrices)):
            if matrices[k][i][j] == 0 or matrices[k][i][j] == 1:
                final_matrix[i][j] = matrices[k][i][j]
                break 


print("\nfinal:")
pmatrix(final_matrix)

