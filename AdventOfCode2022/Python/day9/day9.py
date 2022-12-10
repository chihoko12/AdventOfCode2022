import numpy as np

file = f'day9.txt'
part_1_score = 0
part_2_score = 0


def rope_walk(knots):
    rope = np.zeros((knots+1, 2), dtype='int')

    tails = set()
    tails.add((0, 0))

    for move in moves:
        dir, num = move.split()
        for step in range(int(num)):
            rope[0] += eval(dir)
            for i in range(len(rope)-1):
                diff = rope[i] - rope[i+1]
                if np.any(np.greater(abs(diff), 1)):  # tail needs to move
                    rope[i+1] += np.clip(diff, -1, 1)
                    if i == len(rope) - 2:
                        tails.add((rope[i+1][0], rope[i+1][1]))
    return len(tails)


with open(file) as file:
    moves = file.read().splitlines()

R = np.array([1, 0])
L = np.array([-1, 0])
U = np.array([0, 1])
D = np.array([0, -1])

part_1_score = rope_walk(1)
print(part_1_score)
part_2_score = rope_walk(9)
print(part_2_score)
