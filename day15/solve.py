"""
Advent of code soving CLI
"""

import click

from src import read_input
from src.sensors import n_empty_on_row, tuning_frequency


@click.command()
@click.argument("input_file", type=click.File("r"))
@click.option("--row", type=int, default=2000000)
@click.option("--max-x", type=int, default=4000000)
@click.option("--max-y", type=int, default=4000000)
def solve(input_file, row, max_x, max_y):
    """
    Solve the puzzle for the current day
    """
    input_data = read_input.extract_ints_per_line(input_file)
    click.echo(f"part 1: {n_empty_on_row(input_data, row)}")
    click.echo(f"part 2: {tuning_frequency(input_data, max_x, max_y)}")


if __name__ == "__main__":
    solve()  # pylint: disable=no-value-for-parameter
