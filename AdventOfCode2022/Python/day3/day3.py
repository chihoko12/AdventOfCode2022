alfa = list(map(chr, [*range(97, 123), *range(65, 91)]))
prio = 0
for s in open('day3.in'):
  for x in alfa:
    if x in s[:int(len(s) / 2)] and x in s[int(len(s) / 2):]:
      prio += alfa.index(x)+1
print(prio)

# print(sum([int(list(map(chr, [*range(97, 123), *range(65, 91)])).index(x)+1) for s in open('day3.in')
#       for x in list(map(chr, [*range(97, 123), *range(65, 91)])) if (x in s[:int(len(s) / 2)] and x in s[int(len(s) / 2):])]))

prio = 0
x =  [line.strip() for line in open('day3.in')]
lista = [x[i:i+3] for i in range(0,len(x),3)]
print(lista)
for sub in lista:
  for x in alfa:
    if all(x in sub[i] for i in range(3)):
      prio += alfa.index(x) + 1
print(prio)

print(sum([(list(map(chr, [*range(97, 123), *range(65, 91)])).index(y)+1) for x in list(list(line.strip() for line in open('day3.in'))[i:i+3]
      for i in range(0, len(list(line for line in open('day3.in'))), 3)) for y in (list(map(chr, [*range(97, 123), *range(65, 91)]))) if all(y in x[i] for i in range(3))]))
