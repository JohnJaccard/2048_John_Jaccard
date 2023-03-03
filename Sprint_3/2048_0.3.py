'''
John Jaccard
version du sprint final
03.02.23
0.3
'''
Version = "0.3"
from tkinter import *
import tkinter.font
import random


# tableau 2 dimensions avec des valeurs (4x4)
values_tables = [[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]]

# initiate nmove
nmove = 0

# liste chiffre apparaisable
value_list = [2, 2, 2, 2, 4]

# initiate highscore
text = open("HighScore.txt", "r")
Highscore = text.read()
text.close()

# # fonction pour trier les 0 afin de tasser plus facilement
def move(a, b, c, d):
    global nmove
    if a == 0 and b != 0:
        a, b, c, d = b, c, d, a
        nmove+=1

    if b == 0 and c != 0:
        b, c, d = c, d, b
        nmove+=1

    if c == 0 and d != 0:
        c, d = d, c
        nmove+=1

    if a == 0 and b != 0:
        a, b, c, d = b, c, d, a
        nmove += 1

    if b == 0 and c != 0:
        b, c, d = c, d, b
        nmove+=1

    return a, b, c, d

# fonction pour tasser (aide de léo)
def tasse_4(a,b,c,d):
    global score, nmove, Highscore
    a, b, c, d = move(a, b, c, d)
    # tassage
    if a == b:
        a = a*2
        b = 0
        score += a
        nmove += 1

    if b == c:
        b = b*2
        c = 0
        score += b
        nmove += 1

    if c == d:
        c = c*2
        d = 0
        score += c
        nmove += 1

    if score >= int(Highscore):
        Highscore = score
        text = open("HighScore.txt", "w")
        text.write(str(Highscore))
        text.close()

    a, b, c, d = move(a, b, c, d)
    return [a, b, c, d]


def tass_bind(event):
    global nmove
    # initiate nmove
    Key = event.keysym
    # fonction de tassage assignée à chaque touche
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

    # spawn de 2 à chaque mouvement
    if nmove > 0:
        nmove= 0
        x = random.randint(0, 3)
        y = random.randint(0, 3)
        while values_tables[x][y] != 0:
            x = random.randint(0, 3)
            y = random.randint(0, 3)
        values_tables[x][y] = random.choice(value_list)
        labels[x][y].config(text=values_tables[x][y], bg='black', fg='white')




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
        labels[line][col] = tkinter.Label (width=6, height=3, borderwidth=1, relief="solid", font=("Arial", 30))

        # placement du label dans la fenêtre par ses coordonnées en pixels
        labels[line][col].place(x=30 + width * col, y=120 + height * line)

# bind tass left to left key
fen.bind("<Key>", lambda event: tass_bind(event))

# Score du jeu
Lscore = Label(font=("Arial", 17), bg='#0C343D', fg='white')
LHighScore = Label(font=("Arial", 17),bg='#0C343D', fg='white',text=f'Highscore : {Highscore}')



# function to color labels
def display(values_table):
    global score
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

            Lscore.config(text=f"Score : {score}")
            LHighScore.config(text=f'Highscore : {Highscore}')

display(values_tables)


# fonction new game(aide de Thibault)
def newGame():
    global values_tables,score
    # test de bouton new game mais sans les probabilité avec les 0,2 et 4
    score = 0
    values_tables = [[0, 0, 0, 0],
                     [0, 0, 0, 0],
                     [0, 0, 0, 0],
                     [0, 0, 0, 0]]
    for i in range(2):
        x = random.randint(0, 3)
        y = random.randint(0, 3)
        while values_tables[x][y] !=0:
            x = random.randint(0, 3)
            y = random.randint(0, 3)
        values_tables[x][y] = 2

    # rappel de la fonction display
    display(values_tables)

# start a new game while launching the game
newGame()

# recommencer le jeu
Brestart = Button(text='New game',bg='#0C343D',fg='white',borderwidth=0, command=newGame, activebackground='#0C343D').pack()

Lscore.pack(side=BOTTOM)
LHighScore.pack(side=BOTTOM)



# fin code jeu
fen.mainloop()
