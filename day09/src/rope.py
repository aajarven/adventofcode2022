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


def parse_head_movements(input_lines):
    """
    Return a list of (dx, dy) pairs that represent movements of the rope.
    """
    movements = []
    for line in input_lines:
        numbers = re.findall(r"\d+", line)
        movement_length = int(numbers[0])
        if "R" in line:
            for _ in range(movement_length):
                movements.append((1, 0))
        if "L" in line:
            for _ in range(movement_length):
                movements.append((-1, 0))
        if "U" in line:
            for _ in range(movement_length):
                movements.append((0, 1))
        if "D" in line:
            for _ in range(movement_length):
                movements.append((0, -1))
    return movements


def move_head(rope, movement):
    """
    Move the head of the rope
    """
    rope[0][0] += movement[0]
    rope[0][1] += movement[1]


def move_rope(rope, movement):
    """
    Move the first knot in the rop according to the movement and the rest accordingly.
    """
    move_head(rope, movement)
    for i in range(1, len(rope)):
        knot = rope[i]
        previous = rope[i - 1]
        if not touching(knot, previous):
            if knot[0] < previous[0]:
                knot[0] += 1
            elif knot[0] > previous[0]:
                knot[0] -= 1
            if knot[1] < previous[1]:
                knot[1] += 1
            elif knot[1] > previous[1]:
                knot[1] -= 1


def count_tail_positions_long(input_lines):
    """
    Count tail positions for a long rope with 10 knots
    """
    tail_positions = set()
    head_movements = parse_head_movements(input_lines)
    rope = [[0, 0] for _ in range(10)]
    for movement in head_movements:
        move_rope(rope, movement)
        tail_positions.add(tuple(rope[-1]))
    return len(tail_positions)
