# exemple etiquettes
# JCY jan 2023
# pour comprendre comment on va ajouter dynamiquement des labels

from tkinter import *
import tkinter.font

# tableau 2 dimensions avec des mots (3x3)
words= [["tu", "te", "toi"], ["vous", "votre", "vos"], ["sans", "que", "qui"]]

# tableau 2 dimensions avec des vides qui deviendront des labels.
labels=[[None,None,None],[None,None,None],[None,None,None]]

width=200 #espacement horizontal en pixels des étiquettes (remarque la taille des labels est en caractères)
height=55 #espacement vertical en pixels des étiquettes


# Construction de la fenêtre :
fen = Tk()
fen.geometry("600x480")
fen.title(' exemple étiquettes')

#Création des labels (d'abord on les définit avec =, puis on les place dans la fenêtre avec .place(x,y)
for line in range(len(words)):
    for col in range(len(words[line])):
        # construction de chaque label sans le placer
        labels[line][col] = tkinter.Label (text =words[line][col], width=15, height=2, borderwidth=1, relief="solid", font=("Arial", 15), bg="lightblue")
        # placement du label dans la fenêtre par ses coordonnées en pixels
        labels[line][col].place(x=10 + width * col, y=25 + height * line)

fen.mainloop()
