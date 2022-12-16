class Valve:
    def __init__(self, name, flow_rate=None):
        self.name = name
        self.flow_rate = flow_rate
        self.neighbours = []
        self.opened_on_step = None

    def add_neighbour(self, neighbour):
        if neighbour not in self.neighbours:
            self.neighbours.append(neighbour)

    def __str__(self):
        return f"{self.name} {self.flow_rate}"

    def released_pressure(self, time):
        if self.opened_on_step is None:
            return 0
        return (time - self.opened_on_step) * self.flow_rate
