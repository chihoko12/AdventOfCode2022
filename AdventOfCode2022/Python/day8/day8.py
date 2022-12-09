import numpy as np

with open('day8.txt') as f:
    forest = np.array([[int(x) for x in list(line.strip())] for line in f])


def look_along(x):
    return x > np.hstack((-1, np.maximum.accumulate(x)[:-1]))


is_visible = np.apply_along_axis(look_along, 0, forest)
is_visible |= np.apply_along_axis(look_along, 1, forest)
is_visible |= np.apply_along_axis(look_along, 0, forest[::-1, :])[::-1, :]
is_visible |= np.apply_along_axis(look_along, 1, forest[:, ::-1])[:, ::-1]
print('Day 8, part 1:', is_visible.sum())


def compute_scenic_score(candidate_tree):
    height = forest[candidate_tree]
    row, col = candidate_tree
    if row == 0 or col == 0 or row == forest.shape[0] - 1 or col == forest.shape[1] - 1:
        return 0

    score = (np.maximum.accumulate(forest[row, col + 1:-1]) < height).sum() + 1
    score *= (np.maximum.accumulate(forest[row +
              1:-1, col]) < height).sum() + 1
    score *= (np.maximum.accumulate(forest[row,
              col - 1:0:-1]) < height).sum() + 1
    score *= (np.maximum.accumulate(forest[row -
              1:0:-1, col]) < height).sum() + 1
    return score


scenic_scores = [compute_scenic_score(tree)
                 for tree in zip(*np.nonzero(is_visible))]
print('Day 8, part 2:', np.max(scenic_scores))
