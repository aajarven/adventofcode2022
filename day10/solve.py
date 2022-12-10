"""
Advent of code soving CLI
"""

import click

from src import read_input
from src import cycles


@click.command()
@click.argument("input_file", type=click.File("r"))
def solve(input_file):
    """
    Solve the puzzle for the current day
    """
    input_data = read_input.to_str_lines(input_file)
    click.echo(f"part 1: {cycles.sum_signal_strengths(input_data)}")
    click.echo("part 2:")
    cycles.print_image(input_data)


if __name__ == "__main__":
    solve()  # pylint: disable=no-value-for-parameter
