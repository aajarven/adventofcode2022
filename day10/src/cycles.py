import re


def parse_cycles(input_lines):
    """
    Turn the given input lines into cycle-by-cycle addition values.
    """
    cycle_additions = [0]  # add 0 to make the first cycle the value in index 1
    for line in input_lines:
        cycle_additions.append(0)
        if "addx" in line:
            numbers = re.findall(r"-?\d+", line)
            cycle_additions.append(int(numbers[0]))
    return cycle_additions


def sum_signal_strengths(input_lines):
    """
    Return the sum of signal strenghts during 20 + n*40 cycles.
    """
    cycle_additions = parse_cycles(input_lines)
    cycle = 0
    register = 1
    signal_sum = 0
    while cycle <= 220:
        if (cycle - 20) % 40 == 0:
            signal_sum += (cycle) * register
        register += cycle_additions[cycle]
        cycle += 1
    return signal_sum


def sprite_visible(register, cycle):
    """
    Return True if sprite covers the currently-drawn position
    """
    x_pos = cycle % 40
    if abs(register - x_pos) <= 1:
        return True
    return False


def print_image(input_lines):
    """
    Print the CRT image
    """
    cycle_additions = parse_cycles(input_lines)
    cycle = 0
    register = 1
    while cycle <= 240:
        register += cycle_additions[cycle]
        if sprite_visible(register, cycle):
            print("X", end="")
        else:
            print(".", end="")
        if cycle % 40 == 39:
            print()
        cycle += 1
