import copy
import re

from src.valve import Valve
from src.traversal import Traversal


def extract_valve_names(line):
    return re.findall(r"[A-Z]{2}", line)


def extract_flow_rate(line):
    return int(re.findall(r"\d+", line)[0])


def get_valve_from(valve_dict, valve_name):
    """
    Return a valve with given name from the dict.

    If a valve with the given name is not already present in the dict, one is created
    with default values.
    """
    if valve_name not in valve_dict:
        valve_dict[valve_name] = Valve(valve_name)
    return valve_dict[valve_name]


def parse_valves(input_lines):
    valves = {}
    for line in input_lines:
        valve_names = extract_valve_names(line)
        flow_rate = extract_flow_rate(line)
        valve = get_valve_from(valves, valve_names[0])
        valve.flow_rate = flow_rate

        for neighbour_name in valve_names[1:]:
            neighbour = get_valve_from(valves, neighbour_name)
            valve.add_neighbour(neighbour)
            neighbour.add_neighbour(valve)

    return valves


def releasable_pressure(input_lines):
    valves = parse_valves(input_lines)
    best_pressure = 0

    traversals = [Traversal(copy.deepcopy(valves), "AA", 0)]
    while traversals:
        current = traversals.pop()
        if current.time >= 30:
            if current.released_pressure_at_end > best_pressure:
                best_pressure = current.released_pressure_at_end
                print(best_pressure)
            continue

        for possible_next in current.next_steps():
            traversals.append(possible_next)
    return best_pressure
