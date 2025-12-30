with open("input.txt") as f:
    instr = []
    for raw in f:
        s = raw.strip()
        direction = s[0]
        steps = int(s[1:])
        instr.append([direction, steps])

init = 50
res = 0

for i in range(len(instr)):
    direction, steps = instr[i]    
    prev = init
    
    if direction == "R":
        init = (prev + steps) % 100
        res += (prev + steps) // 100
    elif direction == "L":
        init = (prev - steps) % 100
        if prev == 0:
            res += steps // 100
        else:
            res += ((100 - prev) + steps) // 100

print(res)