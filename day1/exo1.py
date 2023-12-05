f = open('/home/lue/adoctn/day1/input.txt', 'r') 
file = f.read() # file est la cdc contenant le contenu du fichier
f.close() #on ferme proprement

L = file.split("\n") # liste de str
for i in range(len(L)):
    L[i] = list(L[i]) # liste de liste de str
# or les nombres sont ds des quotes donc on les type int

var = 0 # var à renvoyer
for i in range(len(L)): 
    a = "" # str vide
    for j in range(len(L[i])): #on parcourt la liste jusqu'à trouver le premier chf avec un break
        if L[i][j].isdigit():
            a = L[i][j]
            break

    for j in range(len(L[i])): #on parcourt la liste a l'envers, et on concatene avec le cas précédent
        if L[i][-(j+1)].isdigit():
            a += L[i][-(j+1)] # en effet on prends L[-1],L[-2] etc quand on parcourt une liste à l'envers
            break
    var += int(a) # on fait la somme des concaténations qu'on a trad en int

print(var)