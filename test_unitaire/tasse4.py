# Janvier 2023
# création et test unitaire d'une fonction (tasse_4)
# chaque élève doit créer et tester sa fonction (durée environ 4 périodes)


#fait descendre un plot vers le "bas", et fusionne s'il tombe sur un de même valeur
# reçoit 4 nombres, tasse vers le a,  et en renvoie 5
a=[[0,1,2,3],[4,5,6,7,8]]
a[1][1]=230
print(a)

def move(a, b, c, d):
        a,b,c,d=d,c,b,a
        if a==0 and b!=0:
            a,b,c,d=b,c,d,a

        if b == 0 and c!=0:
            b,c,d=c,d,b

        if c == 0 and d!=0:
            c,d=d,c

        if a==0 and b!=0:
            a,b,c,d=b,c,d,a

        if b == 0 and c!=0:
            b,c,d=c,d,b
        a,b,c,d=d,c,b,a
        return a,b,c,d


def tasse_4(a,b,c,d):
    nmove=0
    # ici le code va manipuler a,b,c et d
    # mettre les zéros à droite
    # aide de léo
    a,b,c,d=move(a,b,c,d)
    # tassage
    if a==b:
        a=a*2
        b=0

    if b==c:
        b=b*2
        c=0

    if c==d:
        c=c*2
        d=0
    a, b, c, d=move(a, b, c, d)
    # add movement
    nmove+=1

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
print("................................................................")
print(res)
