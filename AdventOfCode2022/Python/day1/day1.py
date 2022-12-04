# Getting data"
with open('day1_ex.txt') as file :
  data = [i for i in file.read().split("\n")]

cal_count = 0
elf_inventory = []
elf = 0

for i in range(0, len(data)):
  if data[i] == '':
      data[i] = 0
      # add elf x's inventory to the inventory array
      elf_inventory.append(cal_count)
      cal_count = 0  # reset eld cal count to 0.
      elf += 1  # next elf
  else:
    cal_count += int(data[i])    # Adding to the count if its a number

sorted_elf_inventory = sorted(elf_inventory, reverse=True)

# Answers
print("Answer to part 1: %d" %sorted_elf_inventory[0])
print("Answer to part 2: %d" %sum(sorted_elf_inventory[0:3])) # sum top 3 elves

# one line
# print(sum(sorted([sum(list(map(int, bp.splitlines())))
#       for bp in open('day1_ex.txt').read().split('\n\n')], reverse=1)[:3]))
