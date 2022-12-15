class Sensor:
    def __init__(self, sensor_x, sensor_y, beacon_x, beacon_y):
        self.sensor = (sensor_x, sensor_y)
        self.beacon = (beacon_x, beacon_y)
        self.sensing_distance = abs(self.sensor[0] - self.beacon[0]) + abs(
            self.sensor[1] - self.beacon[1]
        )

    def __str__(self):
        return f"Sensor: {self.sensor}, sensing distance {self.sensing_distance}"

    def covers(self, x, y):
        distance = abs(self.sensor[0] - x) + abs(self.sensor[1] - y)
        return distance <= self.sensing_distance

    def reaches_row(self, row_number):
        return abs(self.sensor[1] - row_number) <= self.sensing_distance

    def covered_range_on_row(self, row_number):
        if not self.reaches_row(row_number):
            return []

        distance_to_row = abs(self.sensor[1] - row_number)
        covered_distance_along_row = self.sensing_distance - distance_to_row
        return [
            -1 * covered_distance_along_row + self.sensor[0],
            covered_distance_along_row + self.sensor[0],
        ]

    def covered_locations_on_row(self, row_number):
        endpoints = self.covered_range_on_row(row_number)
        if not endpoints:
            return
        for x in range(endpoints[0], endpoints[1] + 1):
            coordinates = (x, row_number)
            if coordinates == self.beacon:
                continue
            yield coordinates

    def __lt__(self, other):
        leftmost_self = self.sensor[0] - self.sensing_distance
        leftmost_other = other.sensor[0] - other.sensing_distance
        return leftmost_self < leftmost_other
