with open("input.txt", "r") as f:
    lines = []  
    for line in f:
        lines.append(list(line.strip()))

ind = lines[0].index("S")
lines[1][ind] = '|'

res = 0

for i in range(1, len(lines)-1):

    next_line = lines[i+1].copy()
    
    for j in range(len(lines[i])):
        if lines[i][j] == '|':
            if lines[i+1][j] == '^':
                res += 1
                if j > 0:
                    next_line[j-1] = '|'
                if j < len(lines[i]) - 1:
                    next_line[j+1] = '|'

            elif lines[i+1][j] == '.':
                next_line[j] = '|'
            else:
                pass

    lines[i+1] = next_line

print(res)