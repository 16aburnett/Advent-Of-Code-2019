from sys import stdin
import math

def pboard(board, _i, _j):
    offset = 10
    for i in range(_i - offset, _i + offset):
        for j in range(_j - offset, _j + offset):
            print("%  3d" % board[i][j],end="")
        print()

def value(board, pos):
    return board[pos[0]][pos[1]]

def assign(board, pos, val):
    board[pos[0]][pos[1]] = val 


rows = 35000
cols = 35000
board = [[-1 for j in range(cols)] for i in range(rows)]
print("ready")

minsteps = rows*cols+1
count = 1

pos = (rows//2,cols//2)
board[pos[0]][pos[1]] = 0

instructions = input().split(',')

for instruction in instructions:
    dir, num = (instruction[0], int(instruction[1:]))
    print(dir, num)
    if dir == 'U':
        for i in range(num-1):
            pos = (pos[0]-1,pos[1])
            if (value(board,pos) == -1):
                assign(board,pos,count)
            count += 1
        pos = (pos[0]-1,pos[1])
        assign(board, pos, count)
        count += 1
    elif dir == 'R':
        for i in range(num-1):
            pos = (pos[0],pos[1]+1)
            if (value(board,pos) == -1):
                assign(board,pos,count)
            count += 1
        pos = (pos[0],pos[1]+1)
        assign(board, pos, count)
        count += 1
    elif dir == 'D':
        for i in range(num-1):
            pos = (pos[0]+1,pos[1])
            if (value(board,pos) == -1):
                assign(board,pos,count)
            count += 1
        pos = (pos[0]+1,pos[1])
        assign(board, pos, count)
        count += 1
    else: # left
        for i in range(num-1):
            pos = (pos[0],pos[1]-1)
            if (value(board,pos) == -1):
                assign(board,pos,count)
            count += 1
        pos = (pos[0],pos[1]-1)
        assign(board, pos, count)
        count += 1

pos = (rows//2, cols//2)
instructions = input().split(',')
count = 1

for instruction in instructions:
    dir, num = (instruction[0], int(instruction[1:]))
    print(dir, num)
    if dir == 'U':
        for i in range(num):
            pos = (pos[0]-1,pos[1])
            if (value(board,pos) != -1):
                if count + value(board,pos) < minsteps:
                    minsteps = count + value(board,pos)
            count += 1 
    elif dir == 'R':
        for i in range(num):
            pos = (pos[0],pos[1]+1)
            if (value(board,pos) != -1):
                if count + value(board,pos) < minsteps:
                    minsteps = count + value(board,pos)
            count += 1 
    elif dir == 'D':
        for i in range(num):
            pos = (pos[0]+1,pos[1])
            if (value(board,pos) != -1):
                if count + value(board,pos) < minsteps:
                    minsteps = count + value(board,pos)
            count += 1 
    else: # left
        for i in range(num):
            pos = (pos[0],pos[1]-1)
            if (value(board,pos) != -1):
                if count + value(board,pos) < minsteps:
                    minsteps = count + value(board,pos)
            count += 1 

# pboard(board, rows // 2, cols // 2)
print(minsteps)




