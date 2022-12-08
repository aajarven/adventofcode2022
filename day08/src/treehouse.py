def visible_from_left(tree_heights):
    """
    Return array showing whether a tree is visible from the left edge of the forest
    """
    visible = []
    for row in tree_heights:
        visible_on_row = []
        highest_on_row = -1
        for tree in row:
            if tree > highest_on_row:
                visible_on_row.append(True)
                highest_on_row = tree
            else:
                visible_on_row.append(False)
        visible.append(visible_on_row)
    return visible


def visible_from_right(tree_heights):
    """
    Return an array showing whether a tree is visible from the right edge
    """
    visible = []
    for row in tree_heights:
        visible_on_row = []
        highest_on_row = -1
        for tree in row[::-1]:
            if tree > highest_on_row:
                visible_on_row.insert(0, True)
                highest_on_row = tree
            else:
                visible_on_row.insert(0, False)
        visible.append(visible_on_row)
    return visible


def visible_from_top(tree_heights):
    """
    Return an array showing whether a tree is visible from the top edge
    """
    visible = []

    for _ in tree_heights:
        visible.append([])

    for col in range(len(tree_heights[0])):
        highest_on_col = -1
        for row in range(len(tree_heights)):
            if tree_heights[row][col] > highest_on_col:
                visible[row].append(True)
                highest_on_col = tree_heights[row][col]
            else:
                visible[row].append(False)
    return visible


def visible_from_bottom(tree_heights):
    """
    Return an array showing whether a tree is visible from the bottom
    edge
    """
    visible = []

    for _ in tree_heights:
        visible.append([])

    for col in range(len(tree_heights[0])):
        highest_on_col = -1
        for row in range(len(tree_heights) - 1, -1, -1):
            if tree_heights[row][col] > highest_on_col:
                visible[row].append(True)
                highest_on_col = tree_heights[row][col]
            else:
                visible[row].append(False)
    return visible


def count_visible(tree_heights):
    """
    Count the number of trees visible from at least one direction.
    """
    left = visible_from_left(tree_heights)
    right = visible_from_right(tree_heights)
    top = visible_from_top(tree_heights)
    bottom = visible_from_bottom(tree_heights)

    visible = 0
    for i in range(len(tree_heights)):
        for j in range(len(tree_heights[0])):
            if left[i][j] or right[i][j] or top[i][j] or bottom[i][j]:
                visible += 1
    return visible


def scene_left(row, col, tree_heights):
    """
    Determine the scene score to the left of the given tree
    """
    score = 0
    height = tree_heights[row][col]
    col -= 1
    while col >= 0:
        score += 1
        if tree_heights[row][col] >= height:
            return score
        col -= 1
    return score


def scene_right(row, col, tree_heights):
    """
    Determine the scene score to the right of the given tree
    """
    score = 0
    height = tree_heights[row][col]
    col += 1
    while col < len(tree_heights[0]):
        score += 1
        if tree_heights[row][col] >= height:
            return score
        col += 1
    return score


def scene_top(row, col, tree_heights):
    """
    Determine the scene score upwards from the given tree
    """
    score = 0
    height = tree_heights[row][col]
    row -= 1
    while row >= 0:
        score += 1
        if tree_heights[row][col] >= height:
            return score
        row -= 1
    return score


def scene_bottom(row, col, tree_heights):
    """
    Determine the scene score downwards from the given tree
    """
    score = 0
    height = tree_heights[row][col]
    row += 1
    while row < len(tree_heights):
        score += 1
        if tree_heights[row][col] >= height:
            return score
        row += 1
    return score


def scenic_score(row, col, tree_heights):
    """
    Return the scenic score for a specific tree.

    The score is defined as the product of the number of neighboring trees in the four
    cardinal directions up to the first tree that is at least as high as the central
    tree.
    """
    return (
        scene_left(row, col, tree_heights)
        * scene_right(row, col, tree_heights)
        * scene_top(row, col, tree_heights)
        * scene_bottom(row, col, tree_heights)
    )


def best_scenic_score(tree_heights):
    """
    Determine the best scenic score found in the forest
    """
    best = 0
    for row in range(len(tree_heights)):
        for col in range(len(tree_heights)):
            score = scenic_score(row, col, tree_heights)
            if score > best:
                best = score
    return best
