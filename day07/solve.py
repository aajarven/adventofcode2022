"""
Advent of code soving CLI
"""

import click

from src import read_input
from src.parse_cmd import parse_cmd, small_total, smallest_to_remove


@click.command()
@click.argument("input_file", type=click.File("r"))
def solve(input_file):
    """
    Solve the puzzle for the current day
    """
    input_data = read_input.to_str_lines(input_file)
    file_system = parse_cmd(input_data)

    click.echo(f"part 1: {small_total(file_system)}")

    must_free = file_system.size - (70000000 - 30000000)

    click.echo(f"part 2: {smallest_to_remove(file_system, must_free)}")


if __name__ == "__main__":
    solve()  # pylint: disable=no-value-for-parameter
