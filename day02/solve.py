"""
Advent of code soving CLI
"""

import click

from src import read_input
from src.rock_paper_scissors import total_score, total_score_transformed


@click.command()
@click.argument("input_file", type=click.File("r"))
def solve(input_file):
    """
    Solve the puzzle for the current day
    """
    input_data = read_input.to_str_lines(input_file)
    click.echo(f"score using strategy guide: {total_score(input_data)}")
    click.echo(
        f"score using strategy guide and instructions: {total_score_transformed(input_data)}"
    )


if __name__ == "__main__":
    solve()  # pylint: disable=no-value-for-parameter
