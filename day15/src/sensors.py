from src.covered_range import CoveredRange
from src.sensor import Sensor


def n_empty_on_row(input_data, row_number):
    empty_locations = set()
    for row in input_data:
        sensor = Sensor(*row)
        for location in sensor.covered_locations_on_row(row_number):
            empty_locations.add(location)
    return len(empty_locations)


def find_beacon(input_data, max_x, max_y):
    sensors = []
    for row in input_data:
        sensors.append(Sensor(*row))

    covered_ranges = [[] for _ in range(max_y)]
    for sensor in sensors:
        for row in range(0, max_y):
            covered_range = sensor.covered_range_on_row(row)
            if covered_range:
                covered_ranges[row].append(CoveredRange(*covered_range))

    for row_number in range(len(covered_ranges)):
        row = covered_ranges[row_number]
        row.sort()
        covered_end = 0
        for covered_range in row:
            if covered_range.start > 0 and covered_range.start > covered_end + 1:
                return (covered_end + 1, row_number)
            covered_end = max(covered_end, covered_range.end)
        if covered_end < max_x:
            return (covered_end + 1, row_number)


def tuning_frequency(input_data, max_x, max_y):
    beacon = find_beacon(input_data, max_x, max_y)
    return beacon[0] * 4000000 + beacon[1]
