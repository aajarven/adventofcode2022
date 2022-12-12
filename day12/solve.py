"""
Advent of code soving CLI
"""

import click

from src import read_input
from src.maze import find_route_part1, find_route_part2


@click.command()
@click.argument("input_file", type=click.File("r"))
def solve(input_file):
    """
    Solve the puzzle for the current day
    """
    input_data = read_input.to_char_array(input_file)
    click.echo(f"part 1: {find_route_part1(input_data)}")
    click.echo(f"part 2: {find_route_part2(input_data)}")


if __name__ == "__main__":
    solve()  # pylint: disable=no-value-for-parameter
