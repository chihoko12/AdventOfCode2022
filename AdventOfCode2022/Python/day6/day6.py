input = open("day6.txt").read().strip()

def detect(size: int) -> int:
  for i in range((len(input) - size + 1)):
    if len(set(input[i : i + size])) == size:
      break
  return i + size

print(detect(4))
print(detect(14))
