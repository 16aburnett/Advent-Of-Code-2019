# Advent of Code 2019 day 5 part A
# Sunny with a Chance of Asteroids
# By Amy Burnett
import sys
import math

# opcodes
OPCODE_ADD     = 1
OPCODE_MULT    = 2
OPCODE_INPUT   = 3
OPCODE_OUTPUT  = 4
OPCODE_HALT    = 99

# parameter modes
POSITION_MODE  = 0
IMMEDIATE_MODE = 1

# pads icode with 0s to be 5 len 
def pad_zeros(s):
    l = len(s)
    if l == 1:
        return "0000"+s
    elif l == 2:
        return "000"+s
    elif l == 3:
        return "00"+s
    elif l == 4:
        return "0"+s
    else:
        return s

# read in IntCode
memory = list(map(int,input().split(",")))

# give input
INPUT = 1

# run code until halt is reached
code_pointer = 0 

while memory[code_pointer] != OPCODE_HALT:
    # get icode
    icode = pad_zeros(str(memory[code_pointer]))
    # grab components of icode 
    param_mode_1 = int(icode[2])
    param_mode_2 = int(icode[1])
    param_mode_3 = int(icode[0])
    opcode = int(icode[3]+icode[4])
    # opcode 1  : addition
    if (opcode == OPCODE_ADD):
        # grab values
        operand1 = memory[memory[code_pointer+1]] if param_mode_1 == POSITION_MODE else memory[code_pointer+1]
        operand2 = memory[memory[code_pointer+2]] if param_mode_2 == POSITION_MODE else memory[code_pointer+2]
        # grab destination address
        destination = memory[code_pointer+3]
        # perform addition
        memory[destination] = operand1 + operand2
        # advance code_pointer
        code_pointer += 4
    # opcode 2  : multiplication
    elif (opcode == OPCODE_MULT): 
        # grab values
        operand1 = memory[memory[code_pointer+1]] if param_mode_1 == POSITION_MODE else memory[code_pointer+1]
        operand2 = memory[memory[code_pointer+2]] if param_mode_2 == POSITION_MODE else memory[code_pointer+2]
        # grab destination address
        destination = memory[code_pointer+3]
        # perform multiplication
        memory[destination] = operand1 * operand2
        # advance code_pointer
        code_pointer += 4
    # opcode 3 : input 
    elif (opcode == OPCODE_INPUT):
        memory[memory[code_pointer+1]] = INPUT
        # advance code_pointer
        code_pointer += 2 
    # opcode 4 : output 
    elif (opcode == OPCODE_OUTPUT):
        print(memory[memory[code_pointer+1]])
        # advance code_pointer
        code_pointer += 2 
    # unknown opcode : error
    else:
        print("error",opcode,"@",code_pointer)
        print(memory)

print("memory", memory)
print(memory[0])
