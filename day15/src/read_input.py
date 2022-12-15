"""
AoC input reading
"""

import re


def to_str(input_file):
    """
    Return the contents of the file as a single string
    """
    return input_file.read()


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


def per_paragraph_lines(input_file):
    """
    Return input file content as list of paragraphs.

    Each paragraph is a list of lines (as strings) that make up the paragraph.
    Paragraphs are identified as line(s) of text that are separated by an empty line.

    NB: unlike in the per-line input parsing functions, newlines have been stripped from
    the lines
    """
    paragraphs = []
    current_paragraph = []
    for line in input_file:
        if not line.strip():
            paragraphs.append(current_paragraph)
            current_paragraph = []
        else:
            current_paragraph.append(line.strip())

    if current_paragraph:
        paragraphs.append(current_paragraph)

    return paragraphs


def to_digit_array(input_file):
    """
    Read the input file into a 2D array of single-digit integers
    """
    data = []
    for row in to_str_lines(input_file):
        row_digits = []
        for char in row.strip():
            row_digits.append(int(char))
        data.append(row_digits)
    return data


def extract_ints_per_line(input_file):
    """
    Return only integers from the file, ignoring all other content.

    The ints are returned in a list containing a list of ints found on each line.
    """
    ints = []
    for line in to_str_lines(input_file):
        row_ints = [int(int_) for int_ in re.findall(r"-?\d+", line)]
        ints.append(row_ints)
    return ints
