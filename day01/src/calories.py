"""
AoC solution for day 01
"""


def calorie_list(input_strs):
    """
    Construct a list with the calories of each elf in it.
    """
    current_elf_cal = 0
    elf_calories = []
    for line in input_strs:
        if not line.strip():
            elf_calories.append(current_elf_cal)
            current_elf_cal = 0
        else:
            current_elf_cal += int(line)

    if current_elf_cal != 0:
        # for no newline at the end of the file
        elf_calories.append(current_elf_cal)

    return elf_calories


def max_calories(input_strs):
    """
    Return the amount of calories the elf with the most calories has
    """
    elf_calories = calorie_list(input_strs)
    elf_calories.sort()
    return elf_calories[-1]


def top_three_calories(input_strs):
    """
    Return the total amount of calories the three elves with most calories have
    """
    elf_calories = calorie_list(input_strs)
    elf_calories.sort()
    return sum(elf_calories[-3:])
