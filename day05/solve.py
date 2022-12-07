"""
Advent of code soving CLI
"""

import copy

import click

from src import read_input
from src import stack_movements


def split_input(lines):
    """
    Split input into stack lines and operation lines
    """
    split_index = lines.index("\n")
    return (lines[:split_index], lines[split_index + 1 :])


@click.command()
@click.argument("input_file", type=click.File("r"))
def solve(input_file):
    """
    Solve the puzzle for the current day
    """
    input_data = read_input.to_str_lines(input_file)
    (stack_lines, operation_lines) = split_input(input_data)

    stacks = stack_movements.construct_stacks(stack_lines)

    part1_stacks = copy.deepcopy(stacks)
    stack_movements.rearrange_crates_9000(operation_lines, part1_stacks)

    click.echo("part 1: ", nl=False)
    for stack in part1_stacks[1:]:
        click.echo(stack[-1], nl=False)
    click.echo()

    part2_stacks = copy.deepcopy(stacks)
    stack_movements.rearrange_crates_9001(operation_lines, part2_stacks)

    click.echo("part 2: ", nl=False)
    for stack in part2_stacks[1:]:
        click.echo(stack[-1], nl=False)
    click.echo()


if __name__ == "__main__":
    solve()  # pylint: disable=no-value-for-parameter
