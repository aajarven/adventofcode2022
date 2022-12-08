"""
Advent of code soving CLI
"""

import click

from src import read_input
from src.treehouse import count_visible, best_scenic_score


@click.command()
@click.argument("input_file", type=click.File("r"))
def solve(input_file):
    """
    Solve the puzzle for the current day
    """
    input_data = read_input.to_digit_array(input_file)
    click.echo(f"part 1: {count_visible(input_data)}")
    click.echo(f"part 2: {best_scenic_score(input_data)}")


if __name__ == "__main__":
    solve()  # pylint: disable=no-value-for-parameter
