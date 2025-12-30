with open("input.txt") as f:
    r = []
    content = f.read().replace('\n', '')
    for part in content.split(','):
        part = part.strip()
        start, end = part.split('-', 1)        
        r.append([int(start), int(end)])

def repet(nb : int):
    nb = str(nb)
    for i in range(2, len(nb) + 1):
        part = len(nb) // i
        if (len(nb) % i == 0 and nb == nb[:part] * i):
            return True
    return False

res = 0
for i in range(len(r)):
    for j in range(r[i][0], r[i][1] + 1):
        if repet(j):
            res += j

print(res)