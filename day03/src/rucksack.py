def to_priority(char):
    """
    Return priorty for the given character.

    Chars a through z have priorities 1 through 26 and A through Z have priorities 27
    through 52.
    """
    if char.islower():
        return ord(char) - 96
    if char.isupper():
        return ord(char) - 65 + 27

    raise ValueError(f"Character {char} does not seem to be upper or lower case")


def compartmentalize_str(compartment_str):
    """
    Return the priorities of the items in compartment in a list
    """
    compartment = []
    for char in compartment_str:
        compartment.append(to_priority(char))
    return compartment


def parse_rucksack(rucksack_str):
    """
    Turn a rucksack string into a pair of lists showing priorities of the items in
    compartments.
    """
    rucksack_str = rucksack_str.strip()
    compartment_size = int(len(rucksack_str) / 2)
    compartment1_str = rucksack_str[:compartment_size]
    compartment2_str = rucksack_str[compartment_size:]

    return [
        compartmentalize_str(compartment1_str),
        compartmentalize_str(compartment2_str),
    ]


def misplaced_priority(compartment1, compartment2):
    """
    Return the priority of the misplaced item
    """
    # pylint: disable=invalid-name
    compartment1.sort()
    compartment2.sort()
    i1 = 0
    i2 = 0
    while i1 < len(compartment1):
        if compartment1[i1] == compartment2[i2]:
            return compartment1[i1]
        if compartment1[i1] < compartment2[i2]:
            i1 += 1
        else:
            i2 += 1

    raise ValueError(f"No misplaced item found in {compartment1} + {compartment2}")


def total_misplaced_priorities(rucksacks):
    """
    Return the sum of priorities for misplaced items
    """
    total_misplaced = 0
    for rucksack in rucksacks:
        [compartment1, compartment2] = parse_rucksack(rucksack)
        total_misplaced += misplaced_priority(compartment1, compartment2)
    return total_misplaced


def badge_priority(r1, r2, r3):
    """
    Find the badge and return its priority
    """
    # pylint: disable=invalid-name
    for rucksack in [r1, r2, r3]:
        rucksack.sort()
    i1 = i2 = i3 = 0
    while i1 < len(r1):
        if r1[i1] == r2[i2] and r1[i1] == r3[i3]:
            return r1[i1]

        if r1[i1] < r2[i2] and i1 < len(r1) - 1:
            i1 += 1
        elif r2[i2] < r3[i3] and i2 < len(r2) - 1:
            i2 += 1
        else:
            i3 += 1


def total_badge_priorities(rucksacks):
    """
    Return the sum of priorities for badge items
    """
    total_badges = 0
    for i in range(0, len(rucksacks), 3):
        compartmentalized_rucksacks = [
            parse_rucksack(rucksack) for rucksack in rucksacks[i : i + 3]  # noqa
        ]

        unified_rucksacks = [
            rucksack[0] + rucksack[1] for rucksack in compartmentalized_rucksacks
        ]

        total_badges += badge_priority(*unified_rucksacks)
    return total_badges
