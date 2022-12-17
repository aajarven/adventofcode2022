from src.rock import DashRock, PlusRock, LRock, IRock, ORock


class Chamber:
    def __init__(self):
        self.chamber = [[True] * 7]
        self.current_rock = None
        self.rock_loop = self._rock_progression()
        self.rocks = 0

    def __str__(self):
        string = ""
        for row in self.chamber[::-1]:
            for x in row:
                if x:
                    string = string + "#"
                else:
                    string = string + "."
            string += "\n"
        return string

    @property
    def height(self):
        return len(self.chamber) - 1

    @property
    def next_rock_height(self):
        return len(self.chamber) + 3

    def _rock_progression(self):
        while True:
            yield DashRock
            yield PlusRock
            yield LRock
            yield IRock
            yield ORock

    def legal(self, rock_reserved_coordinates):
        for coordinates in rock_reserved_coordinates:
            if coordinates[0] < 0:
                return False
            if coordinates[0] > 6:
                return False
            if coordinates[1] < len(self.chamber):
                if self.chamber[coordinates[1]][coordinates[0]]:
                    return False
        return True

    def _ensure_room_up_to(self, new_height):
        for _ in range(new_height - self.height):
            self.chamber.append([False] * 7)

    def solidify_current_rock(self):
        self._ensure_room_up_to(self.current_rock.max_y)
        for coordinate in self.current_rock.reserved_coordinates:
            self.chamber[coordinate[1]][coordinate[0]] = True
        self.current_rock = None
        self.rocks += 1

    def advance_step(self, wind_direction):
        if not self.current_rock:
            self.current_rock = next(self.rock_loop)(self.next_rock_height)

        next_pos = self.current_rock.next_location(wind_direction)
        if self.legal(next_pos):
            self.current_rock.set_location(next_pos)

        next_pos = self.current_rock.next_location("^")
        if self.legal(next_pos):
            self.current_rock.set_location(next_pos)
        else:
            self.solidify_current_rock()
