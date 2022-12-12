import sys

from src.node import Node


def coordinates_for(match, input_data):
    # pylint: disable=invalid-name,consider-using-enumerate
    for x in range(len(input_data)):
        for y in range(len(input_data[0])):
            if input_data[x][y] == match:
                return (x, y)


def coordinates_for_all(match, input_data):
    # pylint: disable=invalid-name,consider-using-enumerate
    for x in range(len(input_data)):
        for y in range(len(input_data[0])):
            if input_data[x][y] == match:
                yield (x, y)


def create_nodes(input_data, end_coordinates):
    nodes = []
    for x in range(len(input_data)):
        row = []
        for y in range(len(input_data[0])):
            if input_data[x][y] == "S":
                height_char = "a"
            elif input_data[x][y] == "E":
                height_char = "z"
            else:
                height_char = input_data[x][y]
            row.append(Node(x, y, *end_coordinates, height_char))
        nodes.append(row)
    return nodes


def in_grid(x, y, nodes):
    if x < 0:
        return False
    if x >= len(nodes):
        return False
    if y < 0:
        return False
    if y >= len(nodes[0]):
        return False
    return True


def neighbours(x, y, nodes):
    for dx in [-1, 1]:
        new_x = x + dx
        if in_grid(new_x, y, nodes):
            yield (new_x, y)

    for dy in [-1, 0, 1]:
        new_y = y + dy
        if in_grid(x, new_y, nodes):
            yield (x, new_y)


def add_vertices(nodes):
    for x in range(len(nodes)):
        for y in range(len(nodes[0])):
            for neighbour_coordinates in neighbours(x, y, nodes):
                nodes[x][y].add_neighbour(
                    nodes[neighbour_coordinates[0]][neighbour_coordinates[1]]
                )


def construct_map(input_data, end_coordinates):
    nodes = create_nodes(input_data, end_coordinates)
    add_vertices(nodes)
    return nodes


def find_route(start, end, input_data):
    node_map = construct_map(input_data, end)
    start_node = node_map[start[0]][start[1]]
    start_node.g = 0

    nodes = [start_node]

    while nodes:
        current = nodes.pop(0)
        if current.is_goal:
            return current.g

        for neighbour in current.neighbours:
            new_g = current.g + 1
            if neighbour.g > new_g:
                neighbour.g = new_g
                neighbour.previous = current
                if neighbour not in nodes:
                    nodes.append(neighbour)

        nodes.sort()


def find_route_part1(input_data):
    start = coordinates_for("S", input_data)
    end = coordinates_for("E", input_data)
    return find_route(start, end, input_data)


def find_route_part2(input_data):
    starts = []
    starts.append(coordinates_for("S", input_data))
    for low_point in coordinates_for_all("a", input_data):
        starts.append(low_point)

    end = coordinates_for("E", input_data)

    shortest_route = sys.maxsize
    for start in starts:
        route_length = find_route(start, end, input_data)
        if not route_length:
            continue
        if route_length < shortest_route:
            shortest_route = route_length
    return shortest_route
