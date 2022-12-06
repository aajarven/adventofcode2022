"""
Advent of code soving CLI
"""

import click

from src import read_input
from src import signal


@click.command()
@click.argument("input_file", type=click.File("r"))
def solve(input_file):
    """
    Solve the puzzle for the current day
    """
    input_data = read_input.to_str(input_file)
    click.echo(f"part 1: {signal.packet_start(input_data)}")
    click.echo(f"part d: {signal.message_start(input_data)}")


if __name__ == "__main__":
    solve()  # pylint: disable=no-value-for-parameter
