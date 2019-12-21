# Advent of Code 2019 day 7 part A
# Amplification Circuit
# By Amy Burnett
import sys
import math
import itertools

# opcodes
OPCODE_ADD     = 1 
OPCODE_MULT    = 2
OPCODE_INPUT   = 3
OPCODE_OUTPUT  = 4
OPCODE_JMPTRUE = 5
OPCODE_JMPFALSE= 6
OPCODE_LESSTHAN= 7
OPCODE_EQUALS  = 8
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
init_memory = list(map(int,input().split(",")))


def run_intcode(phase_setting, INPUT):

    # print("input",INPUT)
    # print("phase",phase_setting)

    # copy memory
    memory = list(init_memory)

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
        # print("icode",icode)
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
            memory[memory[code_pointer+1]] = phase_setting
            phase_setting = INPUT # cycle next input value
            # advance code_pointer
            code_pointer += 2 
        # opcode 4 : output 
        elif (opcode == OPCODE_OUTPUT):
            # grab params
            param1 = memory[memory[code_pointer+1]] if param_mode_1 == POSITION_MODE else memory[code_pointer+1]
            # output value 
            print("output ->",param1)
            return param1
            # advance code_pointer
            code_pointer += 2 
        # opcode 5 : jump-if-true
        elif (opcode == OPCODE_JMPTRUE):
            # grab params
            param1 = memory[memory[code_pointer+1]] if param_mode_1 == POSITION_MODE else memory[code_pointer+1]
            param2 = memory[memory[code_pointer+2]] if param_mode_2 == POSITION_MODE else memory[code_pointer+2]
            # if param1 is nonzero
            if param1 != 0:
                # jump to the instruction given by param2 
                code_pointer = param2
            # else - dont jump
            else:
                code_pointer += 3
        # opcode 6 : jump-if-false
        elif (opcode == OPCODE_JMPFALSE):
            # grab params
            param1 = memory[memory[code_pointer+1]] if param_mode_1 == POSITION_MODE else memory[code_pointer+1]
            param2 = memory[memory[code_pointer+2]] if param_mode_2 == POSITION_MODE else memory[code_pointer+2]
            # if param1 is zero
            if param1 == 0:
                # jump to the instruction given by param2 
                code_pointer = param2
            # else - dont jump
            else:
                code_pointer += 3
        # opcode 7 : less-than
        elif (opcode == OPCODE_LESSTHAN):
            # grab params
            param1 = memory[memory[code_pointer+1]] if param_mode_1 == POSITION_MODE else memory[code_pointer+1]
            param2 = memory[memory[code_pointer+2]] if param_mode_2 == POSITION_MODE else memory[code_pointer+2]
            # grab destination
            destination = memory[code_pointer+3]
            # logic
            if param1 < param2:
                memory[destination] = 1
            else:
                memory[destination] = 0
            # update code_pointer
            code_pointer += 4
        # opcode 8 : equals
        elif (opcode == OPCODE_EQUALS):
            # grab params
            param1 = memory[memory[code_pointer+1]] if param_mode_1 == POSITION_MODE else memory[code_pointer+1]
            param2 = memory[memory[code_pointer+2]] if param_mode_2 == POSITION_MODE else memory[code_pointer+2]
            # grab destination
            destination = memory[code_pointer+3]
            # logic
            if param1 == param2:
                memory[destination] = 1
            else:
                memory[destination] = 0
            # update code_pointer
            code_pointer += 4
        # unknown opcode : error
        else:
            print("error",opcode,"@",code_pointer)
            print(memory)
    return -1

def run_sequence(seq):
    ans1 = run_intcode(seq[0],    0)
    ans2 = run_intcode(seq[1], ans1)
    ans3 = run_intcode(seq[2], ans2)
    ans4 = run_intcode(seq[3], ans3)
    ans5 = run_intcode(seq[4], ans4)
    return ans5

# generate permutations of the phase setting sequences 
max_thruster_signal = 0 
comb = list(itertools.permutations([0,1,2,3,4],5))

for c in comb:
    print(c)
    output = run_sequence(c)
    print("->",output)
    max_thruster_signal = max(max_thruster_signal, output)

print(max_thruster_signal)