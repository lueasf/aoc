f = open('/home/lue/adoctn/day3/inputy.txt', 'r')
lines = f.readlines()
f.close()

symboles = ["*","#","+","$","%","=","&","/","-","+"] #listes des symboles 
somme = 0 #var finale

for i, line in enumerate(lines):
    j = 0 #pour parcourir la ligne 
    while j < len(line):
        char = line[j] #on garde en mem
        if char.isdigit(): # on regarde si c'est un nombre ou un chiffre
            num_str = char # str
            j += 1
            while j < len(line) and line[j].isdigit():
                num_str += line[j] #on concaten les chiffres pour donner un nombre
                j += 1
            # Vérifier les caractères spéciaux adjacents au nombre
            adjacent_symbols = [lines[x][y] for x in range(i-1, i+2) for y in range(j-len(num_str), j) if 0 <= x < len(lines) and 0 <= y < len(line) and lines[x][y] in symboles]
            #on crée la liste des symboles a coté du chf actuel 
            if any(adjacent_symbols): # et si un nchiffre est a coté, on ajoute le nombre 
                somme += int(num_str)
        else:
            j += 1
print(somme)