with open("input.txt") as f:
    nbs = []
    for line in f.readlines():
        nbs.append(int(line.strip()))

res = 0
for nb in nbs:
    nb = str(nb)
    max1, index1, max2 = max(nb[:-1]), nb.index(max(nb[:-1])), max(nb[nb.index(max(nb[:-1])) + 1 :])
    res += int(max1 + max2)

print(res)