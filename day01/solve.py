"""
Advent of code soving CLI
"""

import click

from src.calories import max_calories, top_three_calories
from src import read_input


@click.command()
@click.argument("input_file", type=click.File("r"))
def solve(input_file):
    """
    Solve the puzzle for the current day
    """
    calorie_strs = read_input.to_str_lines(input_file)
    click.echo(f"max calories: {max_calories(calorie_strs)}")
    click.echo(f"total calories in top three: {top_three_calories(calorie_strs)}")


if __name__ == "__main__":
    solve()  # pylint: disable=no-value-for-parameter
