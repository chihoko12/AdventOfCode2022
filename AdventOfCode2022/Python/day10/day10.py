instructions = open("day10_ex.txt").readlines()

x = 1
c = 0
hist = [x]
output = ""
x_values = dict()

pix = lambda c,x : "#" if abs(c - x) <= 1 else "."

for inst in instructions:
  # output += pix(c,x)
  # c = (c + 1) % 40
  # if inst.startswith("addx"):
  #   output += pix(c,x)
  #   c = (c + 1) % 40
  #   hist.append(x)
  #   x += int(inst.split()[1])
  # hist.append(x)
  if inst.startswith("noop"):
    c += 1
    x_values[c] = x
  else:
    c += 1
    x_values[c] = x
    c += 1
    x_values[c] = x
    x += int(inst.split()[1])

print(sum(x_values[k] * k for k in range(20,221,40)))

# print(sum(i*hist[i-1] for i in range(20,221,40)))
# for row in range(0,6):
#   print(output[row+40:(row+1)*40])

# Part Two
from textwrap import wrap
s = "".join("#" if x_values[c] - 1 <= (c % 40 -1) % 40 <= x_values[c] + 1 else "." for c in range(1,241))
print("\n".join(wrap(s,40)))
