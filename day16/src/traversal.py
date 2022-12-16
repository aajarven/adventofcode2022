import copy


class Traversal:
    def __init__(self, valves, current_valve_name, time):
        self.valves = valves
        self.current_valve_name = current_valve_name
        self.current_valve = self.valves[self.current_valve_name]
        self.time = time

    def next_steps(self):
        # case "we don't open this valve before moving on"
        for neighbour in self.current_valve.neighbours:
            yield Traversal(copy.deepcopy(self.valves), neighbour.name, self.time + 1)

        # case "we open this valve before moving on
        if self.current_valve.flow_rate > 0:
            self.current_valve.opened_on_step = self.time + 1
            for neighbour in self.current_valve.neighbours:
                yield Traversal(
                    copy.deepcopy(self.valves), neighbour.name, self.time + 2
                )

    @property
    def released_pressure_at_end(self):
        return sum(valve.released_pressure(30) for valve in self.valves.values())
