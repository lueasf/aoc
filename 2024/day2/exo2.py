f = open('/home/lue/adoctn/day2/input.txt','r')
lines = f.readlines()
f.close()

somme = 0
for i in range(len(lines)): 
    maxi = { "red" : 0, "blue" : 0, "green" : 0} #utilisation d'un dictionnaire pour garder en memoire les valeurs max
    line = lines[i]
    newline = line.strip().split(":")[1]
    L = newline.split(";")
    somme_l = 0
    for string in L:
        l = string.split(",") #["6 red", "1 blue", "3 green"]
        for x in l:
            val, name = x.split()
            if (int(val) > maxi[name]): # si la valeur est plus faibles que la val actuelles on modifie le dico
                maxi[name] = int(val)
            somme_l = maxi["red"]*maxi["blue"]*maxi["green"] # le power est le produit des trois
    somme = somme + somme_l
print(somme)