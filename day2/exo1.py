f = open('/home/lue/adoctn/day2/input.txt','r')
lines = f.readlines() #liste de str de lignes
f.close()

config = { "blue" : 14, "green" : 13, "red" : 12} # dico config

somme = 0
for i in range(len(lines)): # i représente l'indice
    line = lines[i] # par 
    breaked = False # var pour casser la boucle
    newline = line.strip().split(":")[1] # strip enleve les esp et caract de retour à la ligne ... on garde ce quil y a apres le game
    L = newline.split(";") #on coupe encore les set en sous-liste
    for string in L: #on itère sur chaque set
        l = string.split(",") # on recoupe de la sorte :["60 red", "1 blue", "3 green"]
        for x in l: 
            val, name = x.split() # double affectation pour comparer
            if int(val) > config[name]: # appel au dico config
                breaked = True # si le if est réalisé alors la config est impossible donc 
                break # on sort de la boucle
        if breaked : # on sort de la deuxieme boucle for si breaked est vrai cad si la confi est impossible
            break
    if not breaked: # si on est pas sorti de la boucle la config est valable et on peut sommer
        somme = somme + (i+1) # i+1 pcq les infices démarent à 0 et les games a 1
print(somme)