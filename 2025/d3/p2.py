with open("input.txt") as f:
    nbs = []
    for line in f.readlines():
        nbs.append(int(line.strip()))

# approche pour les enfants
res = 0
for nb in nbs:
    nb = str(nb)
    max1 = max(nb[:-11])
    index1 = nb.index(max1)
    max2 = max(nb[index1 + 1 :-10])
    index2 = nb.index(max2, index1 + 1)
    max3 = max(nb[index2 + 1 :-9])
    index3 = nb.index(max3, index2 + 1)
    max4 = max(nb[index3 + 1 :-8])
    index4 = nb.index(max4, index3 + 1)
    max5 = max(nb[index4 + 1 :-7])
    index5 = nb.index(max5, index4 + 1)
    max6 = max(nb[index5 + 1 :-6])
    index6 = nb.index(max6, index5 + 1)
    max7 = max(nb[index6 + 1 :-5])
    index7 = nb.index(max7, index6 + 1)
    max8 = max(nb[index7 + 1 :-4])
    index8 = nb.index(max8, index7 + 1)
    max9 = max(nb[index8 + 1 :-3])
    index9 = nb.index(max9, index8 + 1)
    max10 = max(nb[index9 + 1 :-2])
    index10 = nb.index(max10, index9 + 1)
    max11 = max(nb[index10 + 1 :-1])
    index11 = nb.index(max11, index10 + 1)
    max12 = max(nb[index11 + 1 :])
    res += int(max1 + max2 + max3 + max4 + max5 + max6 + max7 + max8 + max9 + max10 + max11 + max12)

print(res)

# approche pour les grands enfants
res = 0
for nb in nbs:
    nb = str(nb)

    max_vars = [None] * 12
    index_vars = [None] * 12

    for i in range(12):
        if i == 0:
            slice = nb[:-11]
        elif i < 11:
            prev_index = index_vars[i - 1]
            slice = nb[prev_index + 1 : -(11 - i)]
        else:
            prev_index = index_vars[i - 1]
            slice = nb[prev_index + 1 :]

        max_val = max(slice)

        if i == 0:
            idx = nb.index(max_val)
        else:
            idx = nb.index(max_val, index_vars[i - 1] + 1)

        max_vars[i] = max_val
        index_vars[i] = idx

    max1, max2, max3, max4, max5, max6, max7, max8, max9, max10, max11, max12 = max_vars
    res += int(max1 + max2 + max3 + max4 + max5 + max6 + max7 + max8 + max9 + max10 + max11 + max12)

print(res)