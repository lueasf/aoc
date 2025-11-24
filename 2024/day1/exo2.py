f = open('/home/lue/adoctn/day1/input.txt', 'r') 
file = f.read() # file est la cdc contenant le contenu du fichier
f.close() #on ferme proprement

L = file.split("\n") # liste de str

dictio = { 'one' : 1, 'two' : 2, 'three' : 3, 'four' : 4, 'five' : 5, 'six' : 6, 'seven' : 7, 'eight' : 8, 'nine' : 9}
#dictionnaire associant la str du chiffre au chiffre int

def nombre_in(l):
    newstr = "" #prochaine ch
    temp = "" # on regarde ou on en est
    for c in l:
        if c.isdigit(): # est ce un nb
            newstr += c 
            temp = "" 
        else :
            temp += c #on agrde la ou les cdc 
            for key in dictio: #on regarde si la chaine finit par un nmb str
                if temp.endswith(key):
                    newstr += str(dictio[key])
    return(newstr)

res = 0
for i in L:
    a = nombre_in(i)
    res += int(a[0]+a[-1]) #pour chaque ligne, on renvoie le nm concténé des premiers et derniers
print(res)