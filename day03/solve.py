"""
Advent of code soving CLI
"""

import click

from src import read_input
from src import rucksack


@click.command()
@click.argument("input_file", type=click.File("r"))
def solve(input_file):
    """
    Solve the puzzle for the current day
    """
    input_data = read_input.to_str_lines(input_file)
    click.echo(f"part 1: {rucksack.total_misplaced_priorities(input_data)}")
    click.echo(f"part e: {rucksack.total_badge_priorities(input_data)}")


if __name__ == "__main__":
    solve()  # pylint: disable=no-value-for-parameter
