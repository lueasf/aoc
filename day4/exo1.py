f = open('/home/lue/adoctn/day4/input.txt', 'r') # on ouvre le fichier
lines = f.readlines() # liste avec chaque element egale à une ligne
f.close()

""" lines = ['ligne1', 'ligne2', '...']
    donc la boucle for fait pour i = 0 (exemple):
    sections = "ligne1".split(n) = ['li','ne1']
    et section[0].split() = 'li'.split() = ['li'] pcq ya pas d'espace etc"""

somme = 0
somme_par_ligne = 0
for line in lines: #pour chaque elemtn de la liste on va les metre ds la liste correspondantes 
    somme_par_ligne = 0
    sections = line.split('|') #on transfrm une str en liste de str
    avant = [int(nombre) for nombre in sections[0].split() if nombre.isdigit()]
    apres = [int(nombre) for nombre in sections[1].split() if nombre.isdigit()] 
    for i in apres:
        if i in avant:
            somme_par_ligne += 1
    if somme_par_ligne != 0:
        somme = somme + 2**(somme_par_ligne-1)
print(somme)