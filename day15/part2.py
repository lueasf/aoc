f = open("input.txt","r")
L = f.read().split(",")
f.close()

def hash(str):
    res = 0
    for char in str:
        res += ord(char) # ord renvoie le nb en décimal du char pour la table ascii, chr() pour l'inverse
        res *= 17
        res %= 256
    return res

def part2(Lol):
    res = 0
    L = [[] for _ in range(256)]
    dico = {}
    for mot in Lol:
        if '=' in mot:
            lettres,valeur = mot.split("=")
            h = hash(lettres)
            if lettres not in L[h]:
                L[h].append(lettres)
            dico[lettres] = int(valeur)
        else:
            lettres = mot[:-1]
            h = hash(lettres)
            if lettres in L[h]:
                L[h].remove(lettres)
    for i in range(256):
        for j in range(len(L[i])):
            res += ((i + 1)*(j + 1)*(dico[L[i][j]]))
    return res

print(part2(L))