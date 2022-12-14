# import json

# def cmp(a, b):
#     match(a, b):
#         case int(), int(): return b - a
#         case int(), list(): return cmp([a], b)
#         case list(), int(): return cmp(a, [b])
#         case list(), list():
#             for aa, bb in zip(a, b):
#                 if (r := cmp(aa, bb)) != 0:
#                     return r
#             return len(b) - len(a)
#     assert False

# p1 = 0
# num_smaller = [0, 0]
# for i, pair in enumerate(open("day13_ex.txt").read().strip().split("\n\n")):
#     a, b = [json.loads(s.strip()) for s in pair.split("\n")]
#     if cmp(a, b) > 0:
#         p1 += i + 1
#     for o in (a, b):
#         num_smaller[0] += 1 if cmp(o, [[2]]) > 0 else 0
#         num_smaller[1] += 1 if cmp(o, [[6]]) > 0 else 0
# print(p1)
# print((num_smaller[0] + 1) * (num_smaller[1] + 2))


from functools import cmp_to_key

def right_order(left, right):
    for i in range(min(len(left), len(right))):
        if type(left[i]) == int and type(right[i]) == int:
            if left[i] == right[i]:
                continue
            return left[i] - right[i]
        ret = right_order(
            left[i] if type(left[i]) == list else [left[i]],
            right[i] if type(right[i]) == list else [right[i]]
        )
        if ret:
            return ret
    return len(left) - len(right)

with open("day13.txt") as file:
    packets = [eval(line) for line in file.read().splitlines() if line]
    indices1 = sum(i // 2 + 1 for i in range(0, len(packets), 2) if right_order(*packets[i:i + 2]) < 0)
    packets += [[[2]], [[6]]]
    packets = sorted(packets, key=cmp_to_key(right_order))
    indices2 = (packets.index([[2]]) + 1) * (packets.index([[6]]) + 1)
    print(indices1)
    print(indices2)
