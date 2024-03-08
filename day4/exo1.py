f = open('/home/lue/adoctn/day4/input.txt', 'r')
lines = f.readlines() # liste avec chaque element egale à une ligne
f.close()

somme = 0
somme_par_ligne = 0
for line in lines: #pour chaque elemtn de la liste on va les metre ds la liste correspondantes 
    somme_par_ligne = 0
    sections = line.split('|') #on transfrm une str en liste de str
    avant = [int(nombre) for nombre in sections[0].split() if nombre.isdigit()]
    apres = [int(nombre) for nombre in sections[1].split() if nombre.isdigit()] 
    for i in apres: # pour tout les nombres ds la liste possible
        if i in avant: # on regarde si ils sont ds la liste des gagnants
            somme_par_ligne += 1 # ds ce cas on les compte
    if somme_par_ligne != 0:
        somme = somme + 2**(somme_par_ligne-1) # et on multiplie pas 2 le résultats a chaque nb gagnants
print(somme)