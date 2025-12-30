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

    rge.sort(key=lambda start: start[0])
    merged = [rge[0]]

    for i in range(1, len(rge)):
        curr_start, curr_end = rge[i]
        last_merged_start, last_merged_end = merged[-1]

        if curr_start <= last_merged_end:
            merged[-1] = [last_merged_start, max(last_merged_end, curr_end)]
        else:
            merged.append([curr_start, curr_end])

    len = sum(end - start + 1 for start, end in merged)
    print(len)