"""
Advent of code soving CLI
"""

import click

from src import read_input


@click.command()
@click.argument("input_file", type=click.File("r"))
def solve(input_file):
    """
    Solve the puzzle for the current day
    """
    input_data = read_input.to_str_lines(input_file)
    click.echo(f"part 1: {input_data[0]}")
    click.echo(f"part 2: {input_data[-1]}")


if __name__ == "__main__":
    solve()  # pylint: disable=no-value-for-parameter
