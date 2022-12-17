class Rock:
    def __init__(self, height):
        self.reserved_coordinates = []

    @property
    def max_y(self):
        return max(coordinate[1] for coordinate in self.reserved_coordinates)

    def next_location(self, direction):
        if direction == "<":
            return [
                (location[0] - 1, location[1]) for location in self.reserved_coordinates
            ]
        elif direction == ">":
            return [
                (location[0] + 1, location[1]) for location in self.reserved_coordinates
            ]
        elif direction == "^":
            return [
                (location[0], location[1] - 1) for location in self.reserved_coordinates
            ]

    def set_location(self, new_location):
        self.reserved_coordinates = new_location


class DashRock(Rock):
    def __init__(self, height):
        self.reserved_coordinates = [(2, height), (3, height), (4, height), (5, height)]


class PlusRock(Rock):
    def __init__(self, height):
        self.reserved_coordinates = [
            (3, height),
            (2, height + 1),
            (3, height + 1),
            (4, height + 1),
            (3, height + 2),
        ]


class LRock(Rock):
    def __init__(self, height):
        self.reserved_coordinates = [
            (2, height),
            (3, height),
            (4, height),
            (4, height + 1),
            (4, height + 2),
        ]


class IRock(Rock):
    def __init__(self, height):
        self.reserved_coordinates = [
            (2, height),
            (2, height + 1),
            (2, height + 2),
            (2, height + 3),
        ]


class ORock(Rock):
    def __init__(self, height):
        self.reserved_coordinates = [
            (2, height),
            (3, height),
            (2, height + 1),
            (3, height + 1),
        ]
