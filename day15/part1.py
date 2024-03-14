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

res = 0
for mot in L:
    res += hash(mot)
print(res)