# Advent of Code 2019 day 2 part A
# By Amy Burnett
# IntCode computer
import sys
import math

# opcodes
OPCODE_ADD = 1
OPCODE_MULT = 2
OPCODE_HALT = 99

# read in IntCode
memory = list(map(int,input().split(",")))

# restore to alarm state
memory[1] = 12
memory[2] = 2

# run code until halt is reached
code_pointer = 0 

while memory[code_pointer] != OPCODE_HALT:
    # opcode 1  : addition
    if (memory[code_pointer] == OPCODE_ADD):
        # grab components 
        operand1 = memory[code_pointer+1]
        operand2 = memory[code_pointer+2]
        destination = memory[code_pointer+3]
        # perform addition
        memory[destination] = memory[operand1] + memory[operand2]
        # advance code_pointer
        code_pointer += 4
    # opcode 2  : multiplication
    else: 
        # grab components 
        operand1 = memory[code_pointer+1]
        operand2 = memory[code_pointer+2]
        destination = memory[code_pointer+3]
        # perform multiplication
        memory[destination] = memory[operand1] * memory[operand2]
        # advance code_pointer
        code_pointer += 4

print("memory", memory)
print(memory[0])
