day8data = open("day8data.txt").read().split("\n")
instruction_list = []
instruction_dict = {}
accumulator = 0

for line in day8data:
    instruction_list.append(line.split())

line_number = 1  # set the first line number for the dict

for line in instruction_list:
    instruction_dict[line_number] = line
    line_number += 1


def accumulator_run(acc_value: str) -> int:
    global accumulator
    acc_value_signless = acc_value[1:]
    acc_value_int = int(acc_value_signless)

    if acc_value[0] == "+":
        accumulator += acc_value_int
    elif acc_value[0] == "-":
        accumulator -= acc_value_int

    return 1


def jump_run(jump_value: str) -> int:
    jump_value_new = 0
    jump_value_signless = jump_value[1:]
    jump_value_int = int(jump_value_signless)

    if jump_value[0] == "+":
        jump_value_new += jump_value_int
    elif jump_value[0] == "-":
        jump_value_new -= jump_value_int

    return int(jump_value_new)


def nop_run(value: str) -> int:
    return 1


function_dict = {"acc": accumulator_run, "jmp": jump_run, "nop": nop_run}

# part1
# line = 1  # set the starting line number
# lines_run = []  # create empty list to populate with lines already run

# while True:
#     if line in lines_run:
#         print(accumulator)
#         break

#     instruction = instruction_dict[line][0]
#     instruct_value = instruction_dict[line][1]
#     instruction_executor = function_dict[instruction](instruct_value)

#     if instruction_executor == 1:
#         lines_run.append(line)
#         line += 1

#     else:
#         lines_run.append(line)
#         line += instruction_executor

line = 1  # set the starting line number
lines_run = []  # create empty list to populate with lines already run
changed_instructions = []  # create empty list to populate with line of instruction already attempted changing
instructor_change = False  # bool to indicate if an instruction has been modified

while True:
    if line in lines_run:  # reset the accumulator and line counter
        line = 1
        lines_run = []
        accumulator = 0
        instructor_change = False

    instruction = instruction_dict[line][0]
    instruct_value = instruction_dict[line][1]

    if line not in changed_instructions:
        if instructor_change is False:
            if instruction == "jmp":
                instruction = "nop"
                changed_instructions.append(line)
                instructor_change = True
            elif instruction == "nop":
                instruction = "jmp"
                changed_instructions.append(line)
                instructor_change = True

    instruction_executor = function_dict[instruction](instruct_value)

    if instruction_executor == 1:
        lines_run.append(line)
        line += 1
        if line == len(instruction_list) + 1:
            print(accumulator)
            break

    else:
        lines_run.append(line)
        line += instruction_executor
        if line == len(instruction_list) + 1:
            print(accumulator)
            break
