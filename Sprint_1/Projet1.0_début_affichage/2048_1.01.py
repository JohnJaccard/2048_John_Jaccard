'''
John Jaccard
Premier test d'affichage des labels
03.02.23
1.01
'''
Version = "1.01"
from tkinter import *
import tkinter.font
import random

# tableau 2 dimensions avec des mots (4x4)
words = [[8192, 4096, 2048, 0],[1024, 512, 0, 256],[128, 0, 64, 32],[16, 8, 4, 2],]

# possible values
values = [0,2,4]#,8,16,32,64,128,256,512,1024,2048,4096,8192]

# liste de couleur
colors = {0: '#ffffff', 2: '#FFE3CC', 4: '#DCC3A1', 8: '#03A678', 16: '#02735E', 32: '#F27405', 64: '#FFC2B5', 128: '#8C2656', 256: '#8F797E', 512: '#731702', 1024: '#646C8F', 2048: '#F20544', 4096: '#014040', 8192: '#011836'}

# score de base
score = 0

# tableau 2 dimensions avec des vides qui deviendront des labels.
labels = [[None,None,None,None],[None,None,None,None],[None,None,None,None],[None,None,None,None],]

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
def displaystart(words):
    for line in range(len(words)):
        for col in range(len(words[line])):
            # construction de chaque label sans le placer
            # prendre la couleur selon la valeur de la case
            var = words[line][col]
            color = colors[var]
            textcolor='white'
            # changer la couleur de certaine cases pour améliorer la lisibilité
            if var in [2,4,64]:
                textcolor = 'black'
            # création label
            labels[line][col] = tkinter.Label (text =words[line][col], width=6, height=3, borderwidth=1, relief="solid", font=("Arial", 30), fg=textcolor, bg=color)
            if var == 0:
                labels[line][col].config(text="")
            # placement du label dans la fenêtre par ses coordonnées en pixels
            labels[line][col].place(x=30 + width * col, y=120 + height * line)

# Initialiser l'affichage du jeu
displaystart(words)

# function to randoms label
def display():
    words = [[random.choice(values), random.choice(values), random.choice(values), random.choice(values)],[random.choice(values), random.choice(values), random.choice(values), random.choice(values)],[random.choice(values), random.choice(values), random.choice(values), random.choice(values)],[random.choice(values), random.choice(values), random.choice(values), random.choice(values)],]
    displaystart(words)

# recommencer le jeu
Brestart = Button(text='New game',bg='#0C343D',fg='white',borderwidth=0, command=display, activebackground='#0C343D').pack()



# Score du jeu
Lscore = Label(text=f'Score : {score}', font=("Arial",17),bg='#0C343D',fg='white').pack(side=BOTTOM)

# Essai afin de comprendre le fonctionnement des binds

'''
def test():
    key = event.keysim
    if Key=="Left":
    print("left")
    return 
fen.bind('<Key>', test)'''

# fin code jeu
fen.mainloop()
