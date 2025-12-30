with open("test.txt", "r") as f:
    lines = []  
    for line in f:
        lines.append(line.strip())

    for i in range(len(lines)):
        if '-' in lines[i]:
            start, end = lines[i].split('-')[0], lines[i].split('-')[1]
            lines[i] = [int(start), int(end)]

    ind = lines.index('')
    rge, ids = lines[:ind], lines[ind + 1:]

    res = 0
    for id in ids:
        for rg in rge:
            if int(id) >= rg[0] and int(id) <= rg[1]:
                res += 1
                break

print(res)