"""
Monkey throwing items
"""


class Monkey:
    @classmethod
    def add(cls, op1, op2):
        return op1 + op2

    @classmethod
    def multiply(cls, op1, op2):
        return op1 * op2

    def __init__(
        self,
        items,
        worry_reduction,
        operation_method,
        operand,
        test_divisible,
        monkey_pack,
        true_dest,
        false_dest,
    ):
        self.items = items
        self.worry_reduction = worry_reduction
        self.operation_method = operation_method
        self.operand = operand
        self.test_divisible = test_divisible
        self.monkey_pack = monkey_pack
        self.true_dest = true_dest
        self.false_dest = false_dest
        self.inspections = 0

    def take_turn(self):
        for item in self.items:
            self.inspections += 1
            current_worry = item
            if self.operand == "old":
                current_worry = self.operation_method(item, item)
            else:
                current_worry = self.operation_method(item, self.operand)
            current_worry = current_worry // self.worry_reduction
            current_worry = current_worry % (2 * 3 * 5 * 7 * 11 * 13 * 17 * 19)

            if current_worry % self.test_divisible == 0:
                self.monkey_pack[self.true_dest].give(current_worry)
            else:
                self.monkey_pack[self.false_dest].give(current_worry)
        self.items = []

    def give(self, item):
        self.items.append(item)

    def __str__(self):
        return f"Items: {self.items}"
