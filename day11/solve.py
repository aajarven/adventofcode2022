"""
Advent of code soving CLI
"""

import click

from src import read_input
from src.handle_monkeys import parse_monkeys, monkey_business


@click.command()
@click.argument("input_file", type=click.File("r"))
def solve(input_file):
    """
    Solve the puzzle for the current day
    """
    monkey_specs = read_input.per_paragraph_lines(input_file)
    monkeys = parse_monkeys(monkey_specs, worry_reduction=3)
    click.echo(f"part 1: {monkey_business(monkeys, 20)}")
    monkeys = parse_monkeys(monkey_specs, worry_reduction=1)
    click.echo(f"part 2: {monkey_business(monkeys, 10000)}")


if __name__ == "__main__":
    solve()  # pylint: disable=no-value-for-parameter
