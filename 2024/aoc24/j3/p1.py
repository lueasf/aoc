import re

file = open('input.txt', 'r')
lines = file.readlines()
file.close()

somme = 0
pattern = re.compile(r'mul\((\d+),(\d+)\)')

for line in lines:
    matches = pattern.findall(line) # affiche les tuples (x, y)
    for match in matches:
        x, y = map(int, match)
        somme += x * y

print(somme)