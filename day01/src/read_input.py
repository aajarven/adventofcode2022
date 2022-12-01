"""
AoC input reading
"""


def to_str_lines(input_file):
    """
    Return input file content as a list of strings.

    Each line in file is one element in the list.
    """
    return input_file.readlines()


def to_int_lines(input_file):
    """
    Return input file content as a list of ints.

    Each line in file is one element in the list.
    """
    return [int(line) for line in input_file.readlines()]
