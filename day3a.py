from sys import stdin
import math

def pboard(board, _i, _j):
    offset = 25
    for i in range(_i - offset, _i + offset):
        for j in range(_j - offset, _j + offset):
            print(board[i][j],end="")
        print()

def value(board, pos):
    return board[pos[0]][pos[1]]

def assign(board, pos, val):
    board[pos[0]][pos[1]] = val 


rows = 35000
cols = 35000
board = [['.' for j in range(cols)] for i in range(rows)]
print("ready")
# R75,D30,R83,U83,L12,D49,R71,U7,L72
# U62,R66,U55,R34,D71,R55,D58,R83
# R8,U5,L5,D3
# U7,R6,D4,L4

intersection = max(rows,cols) + 1

pos = (rows//2,cols//2)
board[pos[0]][pos[1]] = '0'

instructions = input().split(',')

for instruction in instructions:
    dir, num = (instruction[0], int(instruction[1:]))
    print(dir, num)
    if dir == 'U':
        for i in range(num):
            pos = (pos[0]-1,pos[1])
            if (value(board,pos) == '.'):
                assign(board,pos,'|')
        assign(board, pos, '+')
    elif dir == 'R':
        for i in range(num):
            pos = (pos[0],pos[1]+1)
            if (value(board,pos) == '.'):
                assign(board,pos,'-')
        assign(board, pos, '+')
    elif dir == 'D':
        for i in range(num):
            pos = (pos[0]+1,pos[1])
            if (value(board,pos) == '.'):
                assign(board,pos,'|')
        assign(board, pos, '+')
    else: # left
        for i in range(num):
            pos = (pos[0],pos[1]-1)
            if (value(board,pos) == '.'):
                assign(board,pos,'-')
        assign(board, pos, '+')

pos = (rows//2, cols//2)
instructions = input().split(',')

for instruction in instructions:
    dir, num = (instruction[0], int(instruction[1:]))
    print(dir, num)
    if dir == 'U':
        for i in range(num):
            pos = (pos[0]-1,pos[1])
            if (value(board,pos) == '.'):
                assign(board,pos,'|')
            else: 
                assign(board,pos,'X')
                intersection = min(intersection, abs(pos[0]-rows//2) + abs(pos[1]-cols//2))
        assign(board, pos, '+')
    elif dir == 'R':
        for i in range(num):
            pos = (pos[0],pos[1]+1)
            if (value(board,pos) == '.'):
                assign(board,pos,'-')
            else: 
                assign(board,pos,'X')
                intersection = min(intersection, abs(pos[0]-rows//2) + abs(pos[1]-cols//2))
        assign(board, pos, '+')
    elif dir == 'D':
        for i in range(num):
            pos = (pos[0]+1,pos[1])
            if (value(board,pos) == '.'):
                assign(board,pos,'|')
            else: 
                assign(board,pos,'X')
                intersection = min(intersection, abs(pos[0]-rows//2) + abs(pos[1]-cols//2))
        assign(board, pos, '+')
    else: # left
        for i in range(num):
            pos = (pos[0],pos[1]-1)
            if (value(board,pos) == '.'):
                assign(board,pos,'-')
            else: 
                assign(board,pos,'X')
                intersection = min(intersection, abs(pos[0]-rows//2) + abs(pos[1]-cols//2))
        assign(board, pos, '+')

pboard(board, rows // 2, cols // 2)
print(intersection)