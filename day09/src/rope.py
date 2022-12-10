import re


def new_head_position(old, movement):
    """
    Calculate head position after the specified momevent
    """
    numbers = re.findall(r"\d+", movement)
    movement_length = int(numbers[0])
    if "R" in movement:
        return (old[0] + movement_length, old[1])
    if "L" in movement:
        return (old[0] - movement_length, old[1])
    if "U" in movement:
        return (old[0], old[1] + movement_length)
    if "D" in movement:
        return (old[0], old[1] - movement_length)

    raise ValueError(f"Malformed movement {movement} encountered")


def touching(head, tail):
    """
    Return True if the head and tail overlap or touch (diagonally ok too)
    """
    return abs(head[0] - tail[0]) <= 1 and abs(head[1] - tail[1]) <= 1


def move_tail(old_tail, head, tail_positions):
    """
    Move the tail towards the head until they touch, return the new position.

    All visited positions are added to tail_positions.
    """
    tail = [old_tail[0], old_tail[1]]
    while not touching(head, tail):
        if tail[0] < head[0]:
            tail[0] += 1
        elif tail[0] > head[0]:
            tail[0] -= 1
        if tail[1] < head[1]:
            tail[1] += 1
        elif tail[1] > head[1]:
            tail[1] -= 1
        tail_positions.add((tail[0], tail[1]))
    return (tail[0], tail[1])


def count_tail_positions(input_lines):
    """
    Return the number of different positions the tail has
    """
    head = (0, 0)
    tail = (0, 0)
    tail_positions = {tail}
    for line in input_lines:
        head = new_head_position(head, line.strip())
        tail = move_tail(tail, head, tail_positions)

    return len(tail_positions)
