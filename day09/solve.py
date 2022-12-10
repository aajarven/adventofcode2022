"""
Advent of code soving CLI
"""

import click

from src import read_input
from src.rope import count_tail_positions, count_tail_positions_long


@click.command()
@click.argument("input_file", type=click.File("r"))
def solve(input_file):
    """
    Solve the puzzle for the current day
    """
    input_data = read_input.to_str_lines(input_file)
    click.echo(f"part 1: {count_tail_positions(input_data)}")
    click.echo(f"part 2: {count_tail_positions_long(input_data)}")


if __name__ == "__main__":
    solve()  # pylint: disable=no-value-for-parameter
