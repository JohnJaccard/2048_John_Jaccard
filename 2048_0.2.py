'''
John Jaccard
Sprint 2 2048
03.02.23
0.2
'''
Version = "0.2"
from tkinter import *
import tkinter.font
import random

# tableau 2 dimensions avec des mots (4x4)
'''values_tables = [[8192, 4096, 0, 2048],
                 [1024, 512, 0, 256],
                 [128, 0, 64, 32],
                 [16, 8, 4, 2]]'''
values_tables = [[0, 0, 0, 2],
                 [2, 0, 2, 2],
                 [2, 2, 2, 2],
                 [0, 0, 2, 2]]


# function to tass
def move(a, b, c, d):
    if a == 0 and b != 0:
        a,b,c,d = b,c,d,a

    if b == 0 and c!=0:
        b,c,d=c,d,b

    if c == 0 and d != 0:
        c, d = d, c

    if a == 0 and b != 0:
        a, b, c, d = b, c, d, a

    if b == 0 and c != 0:
        b, c, d = c, d, b

    return a, b, c, d

def tasse_4(a,b,c,d):
    global score
    # mettre les zéros à droite
    # aide de léo
    a, b, c, d = move(a, b, c, d)
    # tassage
    if a == b:
        a = a*2
        b = 0
        score += a

    if b == c:
        b = b*2
        c = 0
        score += b

    if c == d:
        c = c*2
        d = 0
        score += c

    a, b, c, d = move(a, b, c, d)
    return [a, b, c, d]

def tass(event):
    Key = event.keysym
    if Key == "Left" or Key == "a":
        for line in range(4):
            temp = tasse_4(values_tables[line][0], values_tables[line][1], values_tables[line][2], values_tables[line][3])
            values_tables[line][0] = temp[0]
            values_tables[line][1] = temp[1]
            values_tables[line][2] = temp[2]
            values_tables[line][3] = temp[3]

    if Key == "Right" or Key == "d":
        for line in range(4):
            temp = tasse_4(values_tables[line][3], values_tables[line][2], values_tables[line][1], values_tables[line][0])
            values_tables[line][3] = temp[0]
            values_tables[line][2] = temp[1]
            values_tables[line][1] = temp[2]
            values_tables[line][0] = temp[3]

    if Key == "Up" or Key == "w":
          for col in range(4):
            temp = tasse_4(values_tables[0][col], values_tables[1][col], values_tables[2][col], values_tables[3][col])
            values_tables[0][col] = temp[0]
            values_tables[1][col] = temp[1]
            values_tables[2][col] = temp[2]
            values_tables[3][col] = temp[3]

    if Key == "Down" or Key == "s":
        for col in range(4):
                temp = tasse_4(values_tables[3][col], values_tables[2][col], values_tables[1][col], values_tables[0][col])
                values_tables[3][col] = temp[0]
                values_tables[2][col] = temp[1]
                values_tables[1][col] = temp[2]
                values_tables[0][col] = temp[3]

    display(values_tables)



# liste de couleur
colors = {0: '#ffffff', 2: '#FFE3CC', 4: '#DCC3A1', 8: '#03A678', 16: '#02735E', 32: '#F27405', 64: '#FFC2B5', 128: '#8C2656', 256: '#8F797E', 512: '#731702', 1024: '#646C8F', 2048: '#F20544', 4096: '#014040', 8192: '#011836'}

# score de base
score = 0

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

# Titre du jeu
Ltitle = Label(text='2048', font=("Arial",40),bg='#0C343D',fg='white').pack(pady=10)

# Création des labels (d'abord on les définit avec =, puis on les place dans la fenêtre avec .place(x,y)
for line in range(len(values_tables)):
    for col in range(len(values_tables[line])):
        # création label
        labels[line][col] = tkinter.Label(width=6, height=3, borderwidth=1, relief="solid", font=("Arial", 30))

        # placement du label dans la fenêtre par ses coordonnées en pixels
        labels[line][col].place(x=30 + width * col, y=120 + height * line)

# bind tass left to left key
fen.bind("<Key>", lambda event: tass(event))

# Score du jeu
Lscore = Label(font=("Arial",17),bg='#0C343D',fg='white')

# function to color labels
def display(values_table):
    for line in range(len(values_tables)):
        for col in range(len(values_tables[line])):

             # prendre la couleur selon la valeur de la case
            var = values_tables[line][col]
            color = colors[var]
            textcolor = 'white'

            # changer la couleur de certaine cases pour améliorer la lisibilité
            if var in [2, 4, 64]:
                textcolor = 'black'

            # modifier le text et la couleur des cases
            labels[line][col].config(text=values_tables[line][col], bg=color, fg=textcolor)
            if var == 0:
                labels[line][col].config(text="")

display(values_tables)


# fonction new game(aide de Thibault)
def newGame():
    global values_tables
    # test de bouton new game mais sans les probabilité avec les 0,2 et 4
    position_possible = [0,1,2,3]
    values_tables = [[0, 0, 0, 0],
                     [0, 0, 0, 0],
                     [0, 0, 0, 0],
                     [0, 0, 0, 0]]
    for i in range(2):
        x = int(random.choice(position_possible))
        y = int(random.choice(position_possible))
        values_tables[x][y] = 2
    # rappel de la fonction display
    display(values_tables)

# recommencer le jeu
Brestart = Button(text='New game',bg='#0C343D',fg='white',borderwidth=0, command=newGame, activebackground='#0C343D').pack()

Lscore.pack(side=BOTTOM)



# fin code jeu
fen.mainloop()
