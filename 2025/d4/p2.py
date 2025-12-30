with open("test.txt", "r") as f:
    lines = [list(line.strip()) for line in f]

res = 0
rows = len(lines)

while True:
    to_remove = []
    for l in range(rows):
        for i in range(len(lines[0])):

            if lines[l][i] != '@':
                continue

            nb_rolls = 0
            if (i > 0 and lines[l][i-1] == '@'):
                nb_rolls += 1
            if (i < len(lines[0])-1 and lines[l][i+1] == '@'):
                nb_rolls += 1
            if (l > 0 and lines[l-1][i] == '@'):
                nb_rolls += 1
            if (l < rows-1 and lines[l+1][i] == '@'):
                nb_rolls += 1

            if (l > 0 and i > 0 and lines[l-1][i-1] == '@'):  # diag gauche haut
                nb_rolls += 1
            if (l > 0 and i < len(lines[0])-1 and lines[l-1][i+1] == '@'): # diag droite haut
                nb_rolls += 1
            if (l < rows-1 and i > 0 and lines[l+1][i-1] == '@'):  # diag gauche bas
                nb_rolls += 1
            if (l < rows-1 and i < len(lines[l])-1 and lines[l+1][i+1] == '@'): # diag droite bas
                nb_rolls += 1
                
            if nb_rolls < 4:
                to_remove.append((l, i))

    if (len(to_remove) == 0):
        break

    for r, c in to_remove:
        lines[r][c] = '.'
        res += 1

print(res)