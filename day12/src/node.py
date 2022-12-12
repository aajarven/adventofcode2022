import sys


class Node:
    # pylint: disable=invalid-name

    def __init__(self, x, y, dest_x, dest_y, height_char):
        # pylint: disable=too-many-arguments
        self.x = x
        self.y = y
        self.dest_x = dest_x
        self.dest_y = dest_y
        self.height = ord(height_char) - ord("a")
        self.g = sys.maxsize
        self.previous = None
        self.neighbours = []

    def height_difference(self, other):
        """
        Return the height difference between this node and a node of the given height
        """
        return other.height - self.height

    def add_neighbour(self, other):
        """
        Add given node to neighbours if it is reachable and not already a neighbour.
        """
        if other in self.neighbours:
            return
        if self.height_difference(other) > 1:
            return
        self.neighbours.append(other)

    @property
    def h(self):
        """
        Estimate of the remaining distance
        """
        return abs(self.x - self.dest_x) + abs(self.y - self.dest_y)

    @property
    def f(self):
        """
        Estimate of the total cost to goal node
        """
        return self.h + self.g

    @property
    def is_goal(self):
        return self.x == self.dest_x and self.y == self.dest_y

    def __str__(self):
        return f"({self.x}, {self.y}), {self.f} = {self.g} + {self.h}"

    def __lt__(self, other):
        """
        Less than operator for f score comparison
        """
        if self.f < other.f:
            return True
        return False

    def __eq__(self, other):
        """
        Determine if nodes are same based on their coordinates
        """
        return self.x == other.x and self.y == other.y
