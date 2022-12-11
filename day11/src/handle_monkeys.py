import re

from src.monkey import Monkey


def extract_items(item_line):
    return [int(worry) for worry in re.findall(r"\d+", item_line)]


def extract_operation(op_line):
    if "*" in op_line:
        return Monkey.multiply
    elif "+" in op_line:
        return Monkey.add

    raise ValueError(f"No operation found in '{op_line}'")


def extract_single_int(line):
    return int(re.findall(r"\d+", line)[0])


def extract_operand(line):
    try:
        return extract_single_int(line)
    except IndexError:
        return "old"


def parse_monkeys(monkey_specs, worry_reduction):
    monkeys = []
    for monkey_spec in monkey_specs:
        monkey = Monkey(
            items=extract_items(monkey_spec[1]),
            worry_reduction=worry_reduction,
            operation_method=extract_operation(monkey_spec[2]),
            operand=extract_operand(monkey_spec[2]),
            test_divisible=extract_single_int(monkey_spec[3]),
            monkey_pack=monkeys,
            true_dest=extract_single_int(monkey_spec[4]),
            false_dest=extract_single_int(monkey_spec[5]),
        )
        monkeys.append(monkey)
    return monkeys


def monkey_business(monkeys, rounds):
    for round_ in range(rounds):
        for monkey in monkeys:
            monkey.take_turn()

    business_values = [monkey.inspections for monkey in monkeys]
    business_values.sort()
    return business_values[-1] * business_values[-2]
