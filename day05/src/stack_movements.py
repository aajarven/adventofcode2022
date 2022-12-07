"""
Day 02 input parsing and stack operations logic
"""

from math import ceil
import re


def stack_lines_to_2d_arr(stack_lines):
    """
    Read stack input lines and parse them into an 2D array containing only the
    meaningful characters.
    """
    stack_data_array = []
    for line in stack_lines:
        stack_layer = [line[i * 4 : i * 4 + 3] for i in range(0, ceil(len(line) / 4))]
        for i in range(len(stack_layer)):
            stack_layer[i] = stack_layer[i].strip("[]\n ")
        stack_data_array.append(stack_layer)
    return stack_data_array


def normalize_stack_data_array(stack_data_array):
    """
    Make each row in the array as long as the (bottom) line with the stack indices.
    """
    n_stacks = len(stack_data_array[-1])
    for i in range(len(stack_data_array)):
        stack_data_array[i] = stack_data_array[i] + [""] * (
            n_stacks - len(stack_data_array[i])
        )


def stackify(stack_data_array):
    """
    Turn stack data array into a list of stacks.
    """
    stacks = []
    stacks.append([])  # there's no stack zero
    for col in range(len(stack_data_array[-1])):
        stack = []
        for row in range(len(stack_data_array) - 2, -1, -1):
            box = stack_data_array[row][col]
            if box:
                stack.append(box)
        stacks.append(stack)
    return stacks


def stack_data_array_from_input(stack_lines):
    """
    Split the input lines into an array of stack information.
    """
    stack_data_array = stack_lines_to_2d_arr(stack_lines)
    normalize_stack_data_array(stack_data_array)

    return stack_data_array


def construct_stacks(stack_lines):
    """
    Return a list of stacks (i.e. lists whose append and pop work as push and pop)
    corresponding to the box stacks in input.
    """
    stack_data_array = stack_data_array_from_input(stack_lines)
    return stackify(stack_data_array)


def move(source, destination, n, stacks):
    """
    Move a single crate
    """
    tmp_stack = []

    for i in range(n):
        tmp_stack.append(stacks[source].pop())

    for i in range(n):
        stacks[destination].append(tmp_stack.pop())


def do_operations_9000(line, stacks):
    """
    Do the operations specified on a single line
    """
    matches = re.findall(r"\d+", line)
    count = int(matches[0])
    source = int(matches[1])
    destination = int(matches[2])

    for _ in range(count):
        move(source=source, destination=destination, n=1, stacks=stacks)


def do_operations_9001(line, stacks):
    """
    Do the operations specified on a single line
    """
    matches = re.findall(r"\d+", line)
    count = int(matches[0])
    source = int(matches[1])
    destination = int(matches[2])

    move(source=source, destination=destination, n=count, stacks=stacks)


def rearrange_crates_9000(operation_lines, stacks):
    """
    Carry out all operations listed in operation_lines on the given stacks.
    """
    for line in operation_lines:
        do_operations_9000(line, stacks)


def rearrange_crates_9001(operation_lines, stacks):
    """
    Carry out all operations using CrateMover 9001
    """
    for line in operation_lines:
        do_operations_9001(line, stacks)


def print_stacks(stacks):
    """
    prettyprint the stacks horizontally
    """
    for stack_index in range(len(stacks) - 1):
        print(f"{stack_index+1}: ", end="")
        for box in stacks[stack_index + 1]:
            print(box, end="")
        print()
    print()
