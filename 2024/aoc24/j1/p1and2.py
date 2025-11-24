f = open('input.txt', 'r')
file = f.readlines()
f.close()

L1, L2, s, s2 = [], [], 0, 0
for i in range(len(file)):
    L1.append(file[i].split()[0])
    L2.append(file[i].split()[1])

L1.sort()
L2.sort()

for i in range(len(L1)):
    s += abs(int(L1[i]) - int(L2[i]))
    s2 += int(L1[i])*L2.count(L1[i]) 

print(s, s2)