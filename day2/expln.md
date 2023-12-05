 # EXPLICATION DE MA SOLUTION

 **-EXO1:**
 
 Pour chaque partie(games) on va regarder dans chacun des sets si le nombres de jetons verts, rouges ou bleus tirés 
 ne sont pas des entiers supérieurs a ceux du dictionnaire dans lequel on stock le nombre maximum de jetons par
 couleurs.
 Dans un premier temps on effectue divers opérations de parsing pour obtenir des listes avec seulement un nombre
 et une couleur par élément.On va encore split pour stocker le nombre et la couleur dans des var différentes
 puis avec des break on va sortir des boucles pour passer a la ligne suivante donc au jeu suivant.
 Si on est pas rentré dans la boucle qui indique qu'une game est impossible alors on somme le numéro du jeu.
 efficace.


 **-EXO2:**
 Ici le principe est quasi le meme, mais on doit renvoyer la somme du produit des trois plus grands nombres
 par games et par couleurs.
 J'utilise un dictionnaire pour comparer les différentes valeurs entière des sets de chaque game puis actualiser
 et faire le produit et la somme. 

 L'exo 1 prends du temps mais l'exo 2 prends 10 minutes