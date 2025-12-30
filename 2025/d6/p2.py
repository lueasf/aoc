# AI Generated from gpt
with open("input.txt") as f:
    lines = [l.rstrip("\n") for l in f]

w = max(map(len, lines))
grid = [list(l.ljust(w)) for l in lines]
nbs, ops = grid[:-1], grid[-1]
h = len(nbs)

def empty(j):
    return ops[j] == " " and all(nbs[i][j] == " " for i in range(h))

res, j = 0, 0
while j < w:
    if empty(j): j += 1; continue
    start = j
    while j < w and not empty(j): j += 1
    end = j - 1
    op = next((ops[c] for c in range(start, end+1) if ops[c] in "+*"), None)
    nums = [int("".join(nbs[i][c] for i in range(h) if nbs[i][c].isdigit()))
            for c in range(end, start-1, -1)
            if any(nbs[i][c].isdigit() for i in range(h))]
    res += sum(nums) if op == "+" else __import__("math").prod(nums)
print(res)
