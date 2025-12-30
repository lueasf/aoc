with open("test.txt") as f:
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
    
    if direction == "R":
        init = (init + steps) % 100
        if init == 0:
            res += 1
    elif direction == "L":
        init = (init - steps) % 100
        if init == 0:
            res += 1

print(res)