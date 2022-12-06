import re


def parse_assignments(line):
    """
    Read the assignment start and end points from a line
    """
    numbers = re.findall(r"\d+", line)
    return [
        {"start": int(numbers[0]), "end": int(numbers[1])},
        {"start": int(numbers[2]), "end": int(numbers[3])},
    ]


def contains(assignment1, assignment2):
    """
    Check whether assignment 1 fully contains assignment 2
    """
    if (
        assignment1["start"] <= assignment2["start"]
        and assignment1["end"] >= assignment2["end"]
    ):
        return True
    return False


def n_containing_pairs(pair_lines):
    """
    Count in how many pairs one of the assignments completely contains the other
    """
    containing_pairs = 0
    for line in pair_lines:
        [assignment1, assignment2] = parse_assignments(line)
        # pylint: disable=arguments-out-of-order
        if contains(assignment1, assignment2):
            containing_pairs += 1
        elif contains(assignment2, assignment1):
            containing_pairs += 1

    return containing_pairs


def overlaps(assignment1, assignment2):
    """
    Check if the two assignments overlap at all
    """
    if (
        assignment1["start"] <= assignment2["start"]
        and assignment1["end"] >= assignment2["start"]
    ):
        return True
    if (
        assignment2["start"] <= assignment1["start"]
        and assignment2["end"] >= assignment1["start"]
    ):
        return True
    return False


def n_overlapping_pairs(pair_lines):
    """
    Count the number of pairs whose assignments overlap at all
    """
    overlapping_pairs = 0
    for line in pair_lines:
        [assignment1, assignment2] = parse_assignments(line)
        if overlaps(assignment1, assignment2):
            overlapping_pairs += 1

    return overlapping_pairs
