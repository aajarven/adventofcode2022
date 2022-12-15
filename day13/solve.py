"""
Advent of code soving CLI
"""

import click

from src import read_input
from src.packets import right_order_indices, decoder_key


@click.command()
@click.argument("input_file", type=click.File("r"))
def solve(input_file):
    """
    Solve the puzzle for the current day
    """
    input_data = read_input.to_str_lines(input_file)
    click.echo(f"part 1: {right_order_indices(input_data)}")
    click.echo(f"part 2: {decoder_key(input_data)}")


if __name__ == "__main__":
    solve()  # pylint: disable=no-value-for-parameter
