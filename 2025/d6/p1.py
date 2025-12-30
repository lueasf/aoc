with open("test.txt") as f:
    lines = []
    for line in f.readlines():
        lines.append(line.strip().replace("    ", " ").replace("   ", " ").replace("  ", " ").replace(" ", ","))

    nbs = [[int(x) if x.isdigit() else x for x in line.split(",")] for line in lines[:-1]]
    ops = [line for line in lines[-1].split(",")]

res = 0
for i in range(len(nbs) - 3):
    for j in range(len(nbs[i])):
        if ops[j] == '*':
            res += (nbs[i][j] * nbs[i+1][j] * nbs[i+2][j] * nbs[i+3][j]) # remove nbs[i+3] for test
        if ops[j] == '+':
            res += (nbs[i][j] + nbs[i+1][j] + nbs[i+2][j] + nbs[i+3][j]) # remove nbs[i+3] for test

print(res)