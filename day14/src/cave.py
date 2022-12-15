def to_coordinates(coordinate_str):
    parts = coordinate_str.split(",")
    return (int(parts[0]), int(parts[1]))


def in_between(start, end):
    if start[0] == end[0]:
        for y in range(min(start[1], end[1]), max(start[1], end[1]) + 1):
            yield (start[0], y)
    else:
        for x in range(min(start[0], end[0]), max(start[0], end[0]) + 1):
            yield (x, start[1])


def parse_cave(input_lines):
    rocks = set()
    for line in input_lines:
        corners = line.split(" -> ")
        corner = to_coordinates(corners[0])
        for i in range(1, len(corners)):
            next_corner = to_coordinates(corners[i])
            for coordinate in in_between(corner, next_corner):
                rocks.add(coordinate)
            corner = next_corner
            i += 1
    return rocks


def next_position(sand_coordinates, cave):
    down = (sand_coordinates[0], sand_coordinates[1] + 1)
    if down not in cave:
        return down
    down_left = (sand_coordinates[0] - 1, sand_coordinates[1] + 1)
    if down_left not in cave:
        return down_left
    down_right = (sand_coordinates[0] + 1, sand_coordinates[1] + 1)
    if down_right not in cave:
        return down_right
    return None


def drop_sand(cave):
    sand_position = (500, 0)
    previous = (500, 0)
    floor = floor_height(cave)
    while True:
        sand_position = next_position(sand_position, cave)
        if sand_position is None:
            if previous == (500, 0):
                return None
            cave.add(previous)
            return previous
        if sand_position[1] > floor:
            return None
        previous = sand_position


def sand_drops_void(input_lines):
    cave = parse_cave(input_lines)
    sand_drop_count = 0
    while drop_sand(cave):
        sand_drop_count += 1
    return sand_drop_count


def floor_height(cave):
    max_y = max(coordinate[1] for coordinate in cave)
    return max_y + 2


def add_floor(cave):
    floor_y = floor_height(cave)
    for x in range(-1 * floor_y - 1, 600 + floor_y):
        cave.add((x, floor_y))


def sand_drops_floor(input_lines):
    cave = parse_cave(input_lines)
    add_floor(cave)

    sand_drop_count = 0
    while drop_sand(cave):
        sand_drop_count += 1
    return sand_drop_count
