'''
John Jaccard
Sprint 2 2048
03.02.23
0.2
'''
# liste import
from tkinter import *
import tkinter.font
import random

# tableau 2 dimensions avec des mots (4x4)
values_tables = [[0, 0, 0, 2],
                 [2, 0, 2, 2],
                 [2, 2, 2, 2],
                 [0, 0, 2, 2]]


# numéro de version
Version = "0.2"

# fonction pour trier les 0 afin de tasser plus facilement
def move(a, b, c, d,nmove):
    if a == 0 and b != 0:
        a, b, c, d = b, c, d, a
        nmove += 1

    if b == 0 and c != 0:
        b, c, d = c, d, b
        nmove += 1

    if c == 0 and d != 0:
        c, d = d, c
        nmove += 1

    if a == 0 and b != 0:
        a, b, c, d = b, c, d, a
        nmove += 1

    if b == 0 and c != 0:
        b, c, d = c, d, b
        nmove += 1

    # retourner abcd et nmove
    return a, b, c, d, nmove

# fonction pour tasser (aide de léo)
def tasse_4(a,b,c,d):
    nmove=0
    # trier les 0
    a, b, c, d, nmove = move(a, b, c, d, nmove)

    # tassage
    if a == b:
        a = a*2
        b = 0
        nmove += 1

    if b == c:
        b = b*2
        c = 0
        nmove += 1

    if c == d:
        c = c*2
        d = 0
        nmove += 1

    # trier les 0
    a, b, c, d, nmove = move(a, b, c, d, nmove)

    # retourner les nouvelles valeurs de abcd
    return [a, b, c, d]


# fonction de tassage assignée à chaque touche
def tass_bind(event):
    Key = event.keysym
    if Key == "Left" or Key == "a" or Key == "A":
        for line in range(4):
            [values_tables[line][0], values_tables[line][1], values_tables[line][2], values_tables[line][3]] = tasse_4(values_tables[line][0], values_tables[line][1], values_tables[line][2], values_tables[line][3])

    if Key == "Right" or Key == "d" or Key == "D":
        for line in range(4):
            [values_tables[line][3], values_tables[line][2], values_tables[line][1], values_tables[line][0]] = tasse_4(values_tables[line][3], values_tables[line][2], values_tables[line][1], values_tables[line][0])

    if Key == "Up" or Key == "w" or Key == "W":
        for col in range(4):
            [values_tables[0][col], values_tables[1][col], values_tables[2][col], values_tables[3][col]] = tasse_4(values_tables[0][col], values_tables[1][col], values_tables[2][col], values_tables[3][col])

    if Key == "Down" or Key == "s" or Key == "S":
        for col in range(4):
             [values_tables[3][col], values_tables[2][col], values_tables[1][col], values_tables[0][col]] = tasse_4(values_tables[3][col], values_tables[2][col], values_tables[1][col], values_tables[0][col])
    display(values_tables)



# dictionnaire de couleur
colors = {0: '#ffffff', 2: '#FFE3CC', 4: '#DCC3A1', 8: '#03A678', 16: '#02735E', 32: '#F27405', 64: '#FFC2B5', 128: '#8C2656', 256: '#8F797E', 512: '#731702', 1024: '#646C8F', 2048: '#F20544', 4096: '#014040', 8192: '#011836'}

# tableau 2 dimensions avec des vides qui deviendront des labels.
labels = [[None, None, None, None],
          [None, None, None, None],
          [None, None, None, None],
          [None, None, None, None]]

width = 150 #espacement horizontal en pixels des étiquettes (remarque la taille des labels est en caractères)
height = 150 #espacement vertical en pixels des étiquettes



# Construction de la fenêtre :
fen = Tk()
fen.title(f'2048 by John Jaccard v{Version}')
sizex = 650
sizey = 775
fen.geometry(f"{sizex}x{sizey}+{int((1920-sizex)/2)}+{int((1080-sizey)/2)}")
fen.config(bg='#0C343D')
fen.resizable(width=False, height=False)

# Label du titre du jeu
Ltitle = Label(text='2048', font=("Arial",40),bg='#0C343D',fg='white').pack(pady=10)

# Création des labels (d'abord on les définit avec =, puis on les place dans la fenêtre avec .place(x,y)
for line in range(len(values_tables)):
    for col in range(len(values_tables[line])):
        # création label
        labels[line][col] = tkinter.Label(width=6, height=3, borderwidth=1, relief="solid", font=("Arial", 30))

        # placement du label dans la fenêtre par ses coordonnées en pixels
        labels[line][col].place(x=30 + width * col, y=120 + height * line)

# bind tass aux touches du clavier
fen.bind("<Key>", lambda event: tass_bind(event))

# fonction pour mettre à jour les couleurs des labels et le texte
def display(values_table):
    for line in range(len(values_tables)):
        for col in range(len(values_tables[line])):

             # prendre la couleur selon la valeur de la case
            var = values_tables[line][col]
            color = colors[var]
            textcolor = 'white'

            # changer la couleur du texte de certaine cases pour améliorer la lisibilité
            if var in [2, 4, 64]:
                textcolor = 'black'

            # modifier le text et la couleur des cases
            labels[line][col].config(text=values_tables[line][col], bg=color, fg=textcolor)
            if var == 0:
                labels[line][col].config(text="")
# rappel fonction display
display(values_tables)


# fonction new game (aide de Thibault) pour recommencer une nouvelle partie
def newGame():
    global values_tables
    values_tables = [[0, 0, 0, 0],
                     [0, 0, 0, 0],
                     [0, 0, 0, 0],
                     [0, 0, 0, 0]]
    # prendre deux positions aléatoires et insérer deux 2
    for i in range(2):
        x = random.randint(0, 3)
        y = random.randint(0, 3)
        # Vérifier que les case soient vides
        while values_tables[x][y] != 0:
            x = random.randint(0, 3)
            y = random.randint(0, 3)
        values_tables[x][y] = 2
    # rappel de la fonction display
    display(values_tables)

# recommencer le jeu
Brestart = Button(text='New game',bg='#0C343D',fg='white',borderwidth=0, command=newGame, activebackground='#0C343D').pack()


# fin code jeu
fen.mainloop()
