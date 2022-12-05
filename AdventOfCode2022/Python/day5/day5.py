def parse_crates(f):
  lines = []
  while '1' not in (line := f.readline()):
    lines.append(line)
  n = int(line.strip().split()[-1])
  crates = []
  for i in range(n):
    crates.append([])
  while lines:
    line = lines.pop()
    for i in range(n):
      p = 1 + 4*i
      if p < len(line) and line[p] != ' ':
        crates[i].append(line[p])
  return crates


def parse_program(f):
  program = []
  while line := f.readline():
    _, k, _, fm, _, to = line.strip().split()
    program.append((int(k), int(fm), int(to)))
  return program


def solve_1(crates, program):
  crates = [crate[:] for crate in crates]
  for k, fm, to in program:
    for i in range(k):
      crates[to-1].append(crates[fm-1].pop())
  return ''.join(crate[-1] for crate in crates)


def solve_2(crates, program):
  crates = [crate[:] for crate in crates]
  for k, fm, to in program:
    tmp = []
    for i in range(k):
      tmp.append(crates[fm-1].pop())
    for i in range(k):
      crates[to-1].append(tmp.pop())
  return ''.join(crate[-1] for crate in crates)


with open("day5.txt") as f:
  crates = parse_crates(f)
  if line := f.readline().strip() != '':
    print('bad input')  # empty line
  program = parse_program(f)
  print(solve_1(crates, program))
  print(solve_2(crates, program))
