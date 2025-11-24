f = open('input.txt', 'r') 
file = f.readlines()
f.close()

safe = 0 
notsafe = []

for i in range(len(file)):
    file[i] = list(map(int, file[i].split()))

for i in range(len(file)):
    if file[i][0] > file[i][1]:
        s = True
        for j in range(len(file[i])-1):
            if file[i][j] - file[i][j+1] not in (1,2,3) or file[i][j] <= file[i][j+1]:
                s = False
                notsafe.append(file[i])
                break
        if s:
            safe += 1

    elif file[i][0] < file[i][1]:
        s = True
        for j in range(len(file[i])-1):
            if file[i][j+1] - file[i][j] not in (1,2,3) or file[i][j] >= file[i][j+1]:
                s = False
                notsafe.append(file[i])
                break
        if s:
            safe += 1

print(safe)