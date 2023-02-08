# Janvier 2023
# création et test unitaire d'une fonction (tasse_4)
# chaque élève doit créer et tester sa fonction (durée environ 4 périodes)


#fait descendre un plot vers le "bas", et fusionne s'il tombe sur un de même valeur
# reçoit 4 nombres, tasse vers le a,  et en renvoie 5
def tasse_4(a,b,c,d):
    nmove=0 #sert à savoir si on a réussi à bouger
    # ici le code va manipuler a,b,c et d
    if(a==0):
        if(b>a):
            a,b=b,a
        elif(c>a):
            a,c=c,a
        elif(d>a):
            a,d=d,a
    if(a==b):
        a=a*2
        b=0
    elif (a==c):
        a=a*2
        c=0
    elif (a==d):
        a=a*2
        d=0

    # if(b==c):
    #     b=b*2
    #     c=0
    # if(c==d):
    #     c=d*2
    #     d=0

    # ici on retourne les cinq valeurs en un tableau
    temp=[a,b,c,d,(str(nmove)+" moves")] #tableau temporaire de fin
    return temp

#Test de la fonction tasse
#On demande 4 valeurs numériques, et on veut comme résultats les 4 valeurs tassées vers a
#et en cinquième résultat on veut le nombre de tassements
a = int(input('entrez une valeur numérique : '))
b = int(input('entrez une valeur numérique : '))
c = int(input('entrez une valeur numérique : '))
d = int(input('entrez une valeur numérique : '))

# on envoie les 4 nombres saisis pour tester la fonction
res=tasse_4(a,b,c,d)

# on affiche le résultat (tableau de 5 valeurs)
print(res)
