def total_score(strategy_guide):
    """
    Calculate score for a strategy guide when right column is plays
    """
    points = 0
    for match in strategy_guide:
        points += match_score(match[2], match[0])

    return points


def total_score_transformed(strategy_guide):
    """
    Calculate total score when right column is outcomes
    """
    points = 0
    for match in strategy_guide:
        outcome = match[2]
        opponent_shape = match[0]
        my_shape = calculate_play(outcome, opponent_shape)
        points += match_score(my_shape, opponent_shape)
    return points


def match_score(my_shape, opponent_shape):
    """
    Calculate score for a match
    """
    return shape_points(my_shape) + outcome_points(my_shape, opponent_shape)


def shape_points(shape):
    """
    X = rock = 1
    Y = paper = 2
    Z = scissors = 3
    """
    if shape == "X":
        return 1
    if shape == "Y":
        return 2
    if shape == "Z":
        return 3

    raise ValueError(f"Unexpected shape '{shape}' encountered")


def outcome_points(my_shape, opponent_shape):
    """
    X = rock
    Y = paper
    Z = scissors

    victory = 6
    draw = 3
    loss = 0
    """
    match_magic_number = (ord(my_shape) - ord(opponent_shape)) % 3

    if match_magic_number == 2:
        return 3
    if match_magic_number == 1:
        return 0
    if match_magic_number == 0:
        return 6

    raise ValueError(f"could not parse match '{my_shape}' vs '{opponent_shape}'")


def calculate_play(outcome, opponent_shape):
    """
    Calculate which of the possible shapes I need to play to reach the outcome.

    X = rock / loss
    Y = paper / draw
    Z = scissors / victory
    """
    magic_number = (ord(opponent_shape) + (ord(outcome) % 3)) % 3

    if magic_number == 0:
        return "Z"
    if magic_number == 1:
        return "X"
    if magic_number == 2:
        return "Y"

    raise ValueError(f"could not find play matching '{outcome}' for '{opponent_shape}'")
