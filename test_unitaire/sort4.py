# Janvier 2023
# test unitaire d'une fonction (sort_4)
# chaque élève tester une fonction buggée
# on propose de tester des valeurs avec de plus en plus de mouvement
  # 1,2,3,4 : rien ne bouge [1,2,3,4,0]
  # 1,1,2,3 : rien ne bouge [1,1,2,3,0]
  # 1,2,4,3 : résultat attendu [1,2,3,4,1]
  # 1,4,3,2 : résultat attendu [1,2,3,4,3]
  # 4,3,1,2 : résultat attendu [1,2,3,4,5]
  # 4,3,2,1 : résultat attendu [1,2,3,4,6]
# puis de la corriger et de la retester



# devrait trier 4 nombres du plus petit au plus grand
# reçoit 4 nombres, tasse vers le a, et en renvoie 5 (avec le nombre de permutations)
def sort_4(a,b,c,d):
    nmove=0 #sert à savoir combien de déplacements
    # ici le code va manipuler a,b,c et d
    # on fait 2 passages en comparant 2 à 2
    if (a>b):
        a,b=b,a #spécialité de Python pour inverser 2 variables
        nmove+=1
    if (b>c):
        b,c=c,b
        nmove+=1
    if (c>d):
        c,d=d,c
        nmove+=1
    if (a>b):
        a,b=b,a #spécialité de Python pour inverser 2 variables
        nmove+=1
    if (b>c):
        b,c=c,b
        nmove+=1
    # if (c>d):
    #     c,d=d,c
    if (a>b):
        a,b=b,a
        nmove+=1

    # ici on retourne les cinq valeurs en un tableau
    temp=[a,b,c,d,nmove] #tableau temporaire de fin
    return temp

#Test de la fonction tasse
#On demande 4 valeurs numériques, et on veut comme résultats les 4 valeurs tassées vers a
#et en cinquième résultat on veut le nombre de tassements
a = int(input('entrez une valeur numérique : '))
b = int(input('entrez une valeur numérique : '))
c = int(input('entrez une valeur numérique : '))
d = int(input('entrez une valeur numérique : '))

# on envoie les 4 nombres saisis pour tester la fonction
res=sort_4(a,b,c,d)

# on affiche le résultat (tableau de 5 valeurs)
print(res)
