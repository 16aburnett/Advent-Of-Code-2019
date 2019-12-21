# Advent of Code 2019 day 9 part A
# Sensor Boost
# By Amy Burnett
import sys
import math

# opcodes
OPCODE_ADD     = 1 
OPCODE_MULT    = 2
OPCODE_INPUT   = 3
OPCODE_OUTPUT  = 4
OPCODE_JMPTRUE = 5
OPCODE_JMPFALSE= 6
OPCODE_LESSTHAN= 7
OPCODE_EQUALS  = 8
OPCODE_BASE    = 9
OPCODE_HALT    = 99

# parameter modes
POSITION_MODE  = 0
IMMEDIATE_MODE = 1
RELATIVE_MODE  = 2

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
# and give an extra 100 memory cells 
memory = list(map(int,input().split(","))) + [0 for i in range(100)]

# give input
INPUT = 1

# holds all the output
OUTPUT = []

# run code until halt is reached
code_pointer = 0 

# the base for relative addresses
relative_base = 0

while memory[code_pointer] != OPCODE_HALT:
    # get icode
    icode = pad_zeros(str(memory[code_pointer]))
    # grab components of icode 
    param_mode_1 = int(icode[2])
    param_mode_2 = int(icode[1])
    param_mode_3 = int(icode[0])
    opcode = int(icode[3]+icode[4])
    print(icode,end=" ")
    # opcode 1  : addition
    if (opcode == OPCODE_ADD):
        # grab values
        param1 = memory[memory[code_pointer+1]] if param_mode_1 == POSITION_MODE else memory[memory[code_pointer+1]+relative_base] if param_mode_1 == RELATIVE_MODE else memory[code_pointer+1]
        param2 = memory[memory[code_pointer+2]] if param_mode_2 == POSITION_MODE else memory[memory[code_pointer+2]+relative_base] if param_mode_2 == RELATIVE_MODE else memory[code_pointer+2]
        # grab destination address
        destination = memory[code_pointer+3] if param_mode_3 == POSITION_MODE else memory[code_pointer+3] + relative_base
        # perform addition
        memory[destination] = param1 + param2
        # advance code_pointer
        code_pointer += 4
        print("add\t",param1,"+",param2,"-> mem[",destination,"]",end="")
    # opcode 2  : multiplication
    elif (opcode == OPCODE_MULT): 
        # grab values
        param1 = memory[memory[code_pointer+1]] if param_mode_1 == POSITION_MODE else memory[memory[code_pointer+1]+relative_base] if param_mode_1 == RELATIVE_MODE else memory[code_pointer+1]
        param2 = memory[memory[code_pointer+2]] if param_mode_2 == POSITION_MODE else memory[memory[code_pointer+2]+relative_base] if param_mode_2 == RELATIVE_MODE else memory[code_pointer+2]
        # grab destination address
        destination = memory[code_pointer+3] if param_mode_3 == POSITION_MODE else memory[code_pointer+3] + relative_base
        # perform multiplication
        memory[destination] = param1 * param2
        # advance code_pointer
        code_pointer += 4
        print("mult\t",param1,"*",param2,"-> mem[",destination,"]",end="")
    # opcode 3 : input 
    elif (opcode == OPCODE_INPUT):
        destination = memory[code_pointer+1] if param_mode_1 == POSITION_MODE else memory[code_pointer+1] + relative_base
        memory[destination] = INPUT
        # advance code_pointer
        code_pointer += 2 
        print("input\t",INPUT,"-> mem[",destination,"]",end="")
    # opcode 4 : output 
    elif (opcode == OPCODE_OUTPUT):
        # grab params
        param1 = memory[memory[code_pointer+1]] if param_mode_1 == POSITION_MODE else memory[memory[code_pointer+1]+relative_base] if param_mode_1 == RELATIVE_MODE else memory[code_pointer+1]
        # output value 
        OUTPUT += [param1]
        # advance code_pointer
        code_pointer += 2 
        print("output\t",param1,end="")
    # opcode 5 : jump-if-true
    elif (opcode == OPCODE_JMPTRUE):
        # grab params
        param1 = memory[memory[code_pointer+1]] if param_mode_1 == POSITION_MODE else memory[memory[code_pointer+1]+relative_base] if param_mode_1 == RELATIVE_MODE else memory[code_pointer+1]
        param2 = memory[memory[code_pointer+2]] if param_mode_2 == POSITION_MODE else memory[memory[code_pointer+2]+relative_base] if param_mode_2 == RELATIVE_MODE else memory[code_pointer+2]
        # if param1 is nonzero
        if param1 != 0:
            # jump to the instruction given by param2 
            code_pointer = param2
        # else - dont jump
        else:
            code_pointer += 3
        print("jmpt\t",param1,"== 0 -> jump to ",param2,end="")
    # opcode 6 : jump-if-false
    elif (opcode == OPCODE_JMPFALSE):
        # grab params
        param1 = memory[memory[code_pointer+1]] if param_mode_1 == POSITION_MODE else memory[memory[code_pointer+1]+relative_base] if param_mode_1 == RELATIVE_MODE else memory[code_pointer+1]
        param2 = memory[memory[code_pointer+2]] if param_mode_2 == POSITION_MODE else memory[memory[code_pointer+2]+relative_base] if param_mode_2 == RELATIVE_MODE else memory[code_pointer+2]
        # if param1 is zero
        if param1 == 0:
            # jump to the instruction given by param2 
            code_pointer = param2
        # else - dont jump
        else:
            code_pointer += 3
        print("jmpf\t",param1,"!= 0 -> jump to ",param2,end="")
    # opcode 7 : less-than
    elif (opcode == OPCODE_LESSTHAN):
        # grab params
        param1 = memory[memory[code_pointer+1]] if param_mode_1 == POSITION_MODE else memory[memory[code_pointer+1]+relative_base] if param_mode_1 == RELATIVE_MODE else memory[code_pointer+1]
        param2 = memory[memory[code_pointer+2]] if param_mode_2 == POSITION_MODE else memory[memory[code_pointer+2]+relative_base] if param_mode_2 == RELATIVE_MODE else memory[code_pointer+2]
        # grab destination
        destination = memory[code_pointer+3] if param_mode_3 == POSITION_MODE else memory[code_pointer+3] + relative_base
        # logic
        if param1 < param2:
            memory[destination] = 1
        else:
            memory[destination] = 0
        # update code_pointer
        code_pointer += 4
        print("less\t",param1,"<",param2,"-> mem[",destination,"]",end="")
    # opcode 8 : equals
    elif (opcode == OPCODE_EQUALS):
        # grab params
        param1 = memory[memory[code_pointer+1]] if param_mode_1 == POSITION_MODE else memory[memory[code_pointer+1]+relative_base] if param_mode_1 == RELATIVE_MODE else memory[code_pointer+1]
        param2 = memory[memory[code_pointer+2]] if param_mode_2 == POSITION_MODE else memory[memory[code_pointer+2]+relative_base] if param_mode_2 == RELATIVE_MODE else memory[code_pointer+2]
        # grab destination
        destination = memory[code_pointer+3] if param_mode_3 == POSITION_MODE else memory[code_pointer+3] + relative_base
        # logic
        if param1 == param2:
            memory[destination] = 1
        else:
            memory[destination] = 0
        # update code_pointer
        code_pointer += 4
        print("equals\t",param1,"<",param2,"-> mem[",destination,"]",end="")
    # opcode 9 : relative base offset
    elif (opcode == OPCODE_BASE):
        # grab params
        param1 = memory[memory[code_pointer+1]] if param_mode_1 == POSITION_MODE else memory[memory[code_pointer+1]+relative_base] if param_mode_1 == RELATIVE_MODE else memory[code_pointer+1]
        # logic 
        relative_base += param1
        # update code_pointer
        code_pointer += 2
        print("relbase\t",relative_base,"+=",param1,end="")
    # unknown opcode : error
    else:
        print("error",opcode,"@",code_pointer)
        print(memory)
    print()

print("memory", memory)
print("outputs =",OUTPUT)