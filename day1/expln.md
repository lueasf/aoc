# EXPLICATION DE MA SOLUTION

**-EXO1:**

l'objectif est de concaténer des chiffres dans des chaines de charactères remplies de lettres et de chiffres aléatoires. 

Au début on importe les chaines de charactères du fichier dans une var et on effectue diverses opérations afin d'avoir une liste de liste avec des str, une lettre par indice.

Comment procéder?
Avec des boucles for on va parcourir chaque sous liste jusqu'à trouver le premier chiffre, une deuxième boucle effecue la meme chose avec la meme liste qu'on parcourt à l'envers. On va tomber sur le premier chiffre qui est en fait le dernier ou meme le premier si il n'y en a qu'un. On va concaténer ces deux chaine de charactère que sont les chiffres. On traduit la concaténation en entier et on va sommer chacune des reponses des sous-listes puis renvoyer le résultat.

**-EXO2:**
autre approche, on parcourt les chaines et on garde en memoire tant qu'on trouve pas une chaine du dictionnaire ou un nombre. Le tout dans une fonction qu'on appelle ensuite avec un for pour concaténer les resultats

temps estimé : 2h pour comprendre les consignes tout coder et faire les commentaires, 
bonus mal lire les consignes = perte de temps de 1h MDR 