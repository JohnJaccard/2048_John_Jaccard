'''
John Jaccard
Première version du 2048 durant le sprint 1
03.02.23
1.01
'''
Version = "1.01"
from tkinter import *
import tkinter.font
import random

# tableau 2 dimensions avec des mots (4x4)
values_tables = [[8192, 4096, 2048, 0],
                 [1024, 512, 0, 256],
                 [128, 0, 64, 32],
                 [16, 8, 4, 2]]

# possible values
values = [0,2,4]

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

#Création des labels (d'abord on les définit avec =, puis on les place dans la fenêtre avec .place(x,y)
for line in range(len(values_tables)):
    for col in range(len(values_tables[line])):
        # création label
        labels[line][col] = tkinter.Label (width=6, height=3, borderwidth=1, relief="solid", font=("Arial", 30))

        # placement du label dans la fenêtre par ses coordonnées en pixels
        labels[line][col].place(x=30 + width * col, y=120 + height * line)

# function to randoms label
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

def newGame():
    global values_tables
    # test de bouton new game mais sans les probabilité avec les 0,2 et 4
    values_tables = [[random.choice(values), random.choice(values), random.choice(values), random.choice(values)],
                     [random.choice(values), random.choice(values), random.choice(values), random.choice(values)],
                     [random.choice(values), random.choice(values), random.choice(values), random.choice(values)],
                     [random.choice(values), random.choice(values), random.choice(values), random.choice(values)]]
    # rappel de la fonction display
    display(values_tables)

# recommencer le jeu
Brestart = Button(text='New game',bg='#0C343D',fg='white',borderwidth=0, command=newGame, activebackground='#0C343D').pack()



# Score du jeu
Lscore = Label(text=f'Score : {score}', font=("Arial",17),bg='#0C343D',fg='white').pack(side=BOTTOM)


# fin code jeu
fen.mainloop()
