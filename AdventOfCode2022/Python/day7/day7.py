class DTree:
  def __init__(self, name, parent=None):
    self.name = name
    self.children = {}
    self.files = {}
    self.parent = parent

  def touch(self, size, name):
    self.files[name] = int(size)

  def mkdir(self, name):
    return self.children.setdefault(name, DTree(name, parent=self))

  @property
  def root(self):
    return self if self.parent is None else self.parent.root

  @property
  def size(self):
    return sum(self.files.values()) + sum(c.size for c in self.children.values())

  def __iter__(self):
    for child in self.children.values():
      yield child
      yield from child


data = open("day7.txt").read().strip().split("\n")
cwd = DTree("/")
for line in data[1:]:
  if line.startswith("dir") or line.startswith("$ ls"):
    continue
  elif line.startswith("$ cd"):
    d = line[5:]
    cwd = cwd.parent if d == ".." else cwd.mkdir(d)
  else:
    cwd.touch(*line.split())

print(sum(c.size for c in cwd.root if c.size < 100000)) # part1
print("required space %d" %(30000000 - (70000000 - cwd.root.size)))

for c in cwd.root:
  if c.size > 30000000 - (70000000 - cwd.root.size):
    print(c.size)

print(sum(c.size for c in cwd.root if c.size > 30000000 - (70000000 - cwd.root.size))) #part2
