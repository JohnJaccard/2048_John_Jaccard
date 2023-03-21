'''
John Jaccard
version du sprint final
03.02.23
0.3
'''
import winsound

Version = "0.3"
from tkinter import *
import tkinter.font
import random
import copy
import json
from tkinter import messagebox

blank_table = [[0, 0, 0, 0],[0, 0, 0, 0],[0, 0, 0, 0],[0, 0, 0, 0]]


# tableau 2 dimensions avec des valeurs (4x4)
values_tables = copy.deepcopy(blank_table)

# save of vaules table
table = 0

# set undo table value
undo_table = copy.deepcopy(values_tables)

# Faire
end_game = False
end_game2 = False

# liste chiffre apparaisable
value_list = [2, 2, 2, 2, 4]

# Prendre le score highscore
text = open("txt\HighScore.txt", "r")
Highscore = int(text.read())
text.close()

# # fonction pour trier les 0 et les mettre les 0 à la fin et pouvoir tasser proprement
def sort(a, b, c, d):
    if a == 0 and b != 0:
        a, b, c, d = b, c, d, a

    if b == 0 and c != 0:
        b, c, d = c, d, b

    if c == 0 and d != 0:
        c, d = d, c

    if a == 0 and b != 0:
        a, b, c, d = b, c, d, a

    if b == 0 and c != 0:
        b, c, d = c, d, b

    return a, b, c, d

# fonction pour tasser (aide de léo)
def tasse_4(a,b,c,d):
    global score
    a, b, c, d = sort(a, b, c, d)
    # tassage si a et b sont identiques il va les tasser et ajouter ce tassement au score
    if a == b:
        a = a*2
        b = 0
        score += a

    # tassage si b et c sont identiques il va les tasser et ajouter ce tassement au score
    if b == c:
        b = b*2
        c = 0
        score += b

    # tassage si c et d sont identiques il va les tasser et ajouter ce tassement au score
    if c == d:
        c = c*2
        d = 0
        score += c

    a, b, c, d = sort(a, b, c, d)
    return [a, b, c, d]


def tass_bind(event):
    global table,undo_table,values_tables,blank_table,undo_score
    # Copie de la table de base
    save_table = copy.deepcopy(values_tables)

    # Copie de la table de base pour le bouton Undo
    undo_table = copy.deepcopy(values_tables)

    # Copie du score pour le bouton Undo
    undo_score = score

    # Assigner la touche à une variable
    Key = event.keysym

    # Fonction de tassage assignée à chaque touche
    if Key == "Left" or Key == "a" or Key == "A":
        for line in range(4):
            [values_tables[line][0], values_tables[line][1], values_tables[line][2], values_tables[line][3]] = tasse_4(values_tables[line][0], values_tables[line][1], values_tables[line][2], values_tables[line][3])

            # Ajout de 1 à une variable si la table à changée
            if save_table != values_tables:
                table += 1

    if Key == "Right" or Key == "d" or Key == "D":
        for line in range(4):
            [values_tables[line][3], values_tables[line][2], values_tables[line][1], values_tables[line][0]] = tasse_4(values_tables[line][3], values_tables[line][2], values_tables[line][1], values_tables[line][0])

            # Ajout de 1 à une variable si la table à changée
            if save_table != values_tables:
                table += 1

    if Key == "Up" or Key == "w" or Key == "W":
        for col in range(4):
            [values_tables[0][col], values_tables[1][col], values_tables[2][col], values_tables[3][col]] = tasse_4(values_tables[0][col], values_tables[1][col], values_tables[2][col], values_tables[3][col])

            # Ajout de 1 à une variable si la table à changée
            if save_table != values_tables:
                table += 1

    if Key == "Down" or Key == "s" or Key == "S":
        for col in range(4):
            [values_tables[3][col], values_tables[2][col], values_tables[1][col], values_tables[0][col]] = tasse_4(values_tables[3][col], values_tables[2][col], values_tables[1][col], values_tables[0][col])

            # Ajout de 1 à une variable si la table à changée
            if save_table != values_tables:
                table += 1

    # Rappel fonction display
    display(values_tables)

    # Spawn de 2 si la table à changée
    if table > 0:
        table = 0
        x = random.randint(0, 3)
        y = random.randint(0, 3)
        while values_tables[x][y] != 0:
            x = random.randint(0, 3)
            y = random.randint(0, 3)
        values_tables[x][y] = random.choice(value_list)
        labels[x][y].config(text=values_tables[x][y], bg='black', fg='white')

    # Prends la game precedemment quittée
    game = open("txt\Gamesave.txt", 'w')
    game.write(str(values_tables))
    game.close()

    # Écrit le score de la partie dans un fichier texte pour que quand on quitte la partie en revenant nous aurons toujours le même score
    score_saving = open("txt\Score.txt", 'w')
    score_saving.write(str(score))
    score_saving.close()

    # Fonction afin de check si la game est finie et si oui afficher l'écran de fin
    check()

# liste de couleur
colors = {0: '#ffffff', 2: '#FFE3CC', 4: '#DCC3A1', 8: '#03A678', 16: '#02735E', 32: '#F27405', 64: '#FFC2B5', 128: '#8C2656', 256: '#8F797E', 512: '#731702', 1024: '#646C8F', 2048: '#F20544', 4096: '#014040', 8192: '#011836'}

# Initialiser le score de base si une partie à été commencée
score_base = open("txt\Score.txt", 'r')
try:
    score = int(score_base.read())
    undo_score = score
except ValueError:
    score = 0
score_base.close()


# tableau 2 dimensions avec des vides qui deviendront des labels.
labels = [[None, None, None, None],
          [None, None, None, None],
          [None, None, None, None],
          [None, None, None, None]]

# Espacement horizontal en pixels des étiquettes (remarque la taille des labels est en caractères)
width = 150

# Espacement vertical en pixels des étiquettes
height = 150

# Construction de la fenêtre :
fen = Tk()
fen.title(f'2048 by John Jaccard v{Version}')
sizex = 650
sizey = 800
fen.geometry(f"{sizex}x{sizey}+{int((1920-sizex)/2)}+{int((1080-sizey)/2)}")
fen.config(bg='#0C343D')
fen.resizable(width=False, height=False)

# to play
# winsound.PlaySound('music.wav', winsound.SND_ASYNC)
# to stop
# winsound.PlaySound(None, winsound.SND_PURGE)

# Titre du jeu
Ltitle = Label(text='2048', font=("Arial",40), bg='#0C343D', fg='white').pack(pady=10)

# Création des labels (d'abord on les définit avec =, puis on les place dans la fenêtre avec .place(x,y)
for line in range(len(values_tables)):
    for col in range(len(values_tables[line])):
        # Création label
        labels[line][col] = tkinter.Label (width=6, height=3, borderwidth=1, relief="solid", font=("Arial", 30))

        # Placement du label dans la fenêtre par ses coordonnées en pixels
        labels[line][col].place(x=30 + width * col, y=120 + height * line)

# Assigner la fonction tass aux touches
fen.bind("<Key>", lambda event: tass_bind(event))

# Score du jeu
Lscore = Label(font=("Arial", 17), bg='#0C343D', fg='white')
LHighScore = Label(font=("Arial", 17),bg='#0C343D', fg='white', text=f'Highscore : {Highscore}')

# Touche afin d'annuler la dernière action
BUndo_image = PhotoImage(file='img\Bundo_img.png')
BUndo = Button( bg='#0C343D', activebackground='#0C343D', borderwidth=0,image=BUndo_image,command=lambda: Undo())

# Image et écran de victoire + le bouton continuer sur l'écran de victoire
win_screen = PhotoImage(file='img\win_screen.png',width=600,height=600)
Lwin_screen = Label(image=win_screen,bg='white')
Bwin = Button(bg='white',fg='black',borderwidth=0, activebackground='white',text="Continue",command=lambda: continue_game(),font=("Ubuntu Mono", 30, "italic"))

# Image et écran de défaite + le bouton continuer sur l'écran de défaite
loose_screen = PhotoImage(file='img\loose_screen.png',width=600,height=600)
Lloose_screen = Label(image=loose_screen,bg='grey')
Bloose = Button(bg='grey',fg='white',borderwidth=0, activebackground='grey',text="Afficher le jeu",command=lambda : loose_game(),font=("Ubuntu Mono", 30, "italic"))

# Fonction afin de revenir une action en arrière dans le jeu
def Undo():
    global values_tables,undo_table,undo_score,score
    values_tables = undo_table
    score = undo_score
    display(values_tables)

# Fonction qui affiche le menu debug
def cheat_screen():
    sizex = 900
    sizey = 800
    fen.geometry(f"{sizex}x{sizey}+{int((1920-sizex)/2)}+{int((1080-sizey)/2)}")
    Bcheat_quit.place(x=750,y=50)
    Lcheat_x_y.place(x=660,y=100)
    Echeat_x.place(x=725,y=120)
    Echeat_y.place(x=775,y=120)
    Lcheat_nb.place(x=690,y=140)
    Echeat_nb.place(x=725,y=160)
    Bcheat_confirm.place(x=730,y=180)
    Bcheat_randomnb.place(x=730,y=220)
    Bcheat_randomcolor.place(x=710,y=250)
    Bclear_highscore.place(x=715,y=300)

# Fonction pour quitter le menu debug
def quit_cheat_screen():
    sizex = 650
    sizey = 800
    fen.geometry(f"{sizex}x{sizey}+{int((1920-sizex)/2)}+{int((1080-sizey)/2)}")

# Bouton afin d'afficher la case avec les coordonnées rentrées en vérifiant si les informations sont correctes
def confirm_cheat_screen():
    global Echeat_x, Echeat_y, Echeat_nb, values_tables
    try:
        x = int(Echeat_x.get())
        y = int(Echeat_y.get())
        nb = int(Echeat_nb.get())
        if x in [0, 1, 2, 3] and y in [0,1,2,3]:
            if nb in [0, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192]:
                values_tables[x][y] = nb
            else:
                messagebox.showerror("Erreur", "Nombre invalide")
        else:
            messagebox.showerror("Erreur", "Coordonnées invalides")

    except ValueError:
        messagebox.showerror("Erreur", "Veuillez saisir un nombre valide")
    display(values_tables)

# Fonction afin de convertir de code rgb en hexa la couleur
def rgb_to_hexa(rgb):
    return "#%02x%02x%02x" % rgb

# Fonction afin d'arrêter les couleur multicolore et remettre ensuite la fonction de base
def randomcoloroff():
    global Random_color,Bcheat_randomcolor,values_tables
    Random_color = 0
    Bcheat_randomcolor.config(command=lambda: randomcolorcheck())
    display(values_tables)

# Cette fonction génère trois valeur de 0 a 255 pour chaque case du tableau et les appliquent
# A la fin il change le bouton afin que en réappuyant on arrête le mode rainbow
def cheat_randomcolor_screen():
    global values_tables,Ccheat_randomcolor,Random_color
    for line in range(len(values_tables)):
        for col in range(len(values_tables[line])):
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            rgb = (r, g, b)
            rgb = rgb_to_hexa(rgb)
            labels[line][col].config(text=values_tables[line][col], bg=rgb)
            if values_tables[line][col] == 0:
                labels[line][col].config(text="")
    Bcheat_randomcolor.config(command=lambda: randomcoloroff())

# Lance en boucle la fonction randomcolorcheck avec un temps entre chaque fois et sinon le réactive pour le prochain appuie
def randomcolorcheck():
    global Random_color
    if Random_color == 1:
        cheat_randomcolor_screen()
        fen.after(4, randomcolorcheck)
    else:
        Random_color = 1

# Fonction permettant de random la position de tout les tuiles avec une valeur
def random_cheat_screen():
    global values_tables
    values = []
    for i in values_tables:
        for y in i:
            values.append(y)
    values_tables = copy.deepcopy(blank_table)
    for j in values:
        x = random.randint(0, 3)
        y = random.randint(0, 3)
        while values_tables[x][y] != 0:
            x = random.randint(0, 3)
            y = random.randint(0, 3)
        values_tables[x][y] = j
    display(values_tables)

def clear_highscore():
    global Highscore
    Highscore = 0
    display(values_tables)

# Bouton permettant dâfficher le menu de spawn de tuile
Bcheat = Button(text='DEBUG',bg='#0C343D',fg='#0C343D',borderwidth=0, command=lambda: cheat_screen())

# Bouton permettant de quitter le menu de spawn de tuile
Bcheat_quit = Button(text='Exit',bg='#0C343D',fg='white',borderwidth=0, command=lambda: quit_cheat_screen())

# Label et entrées pour le remplissage des coordonnées
Lcheat_x_y = Label(text='Veuillez indiquez des coords entre 0 et 3',bg='#0C343D',fg='white',borderwidth=0)
Echeat_x = Entry(width=2)
Echeat_y = Entry(width=2)

# Label et entrée pour demander le nombre à spawn
Lcheat_nb = Label(text='Veuillez insérer le nb à placer',bg='#0C343D',fg='white',borderwidth=0)
Echeat_nb = Entry(width=10)

# Bouton afin de confirmer le nombre et les coordonnées rentrées en vérifiant si elles sont correctes et afficher la case
Bcheat_confirm = Button(text='Confirm', bg='#0C343D', fg='white',borderwidth=0, command=lambda: confirm_cheat_screen())

# Bouton relié à une fonction qui permet de random tout les nombres existant et les replacer
Bcheat_randomnb = Button(text='Random', bg='#0C343D', fg='white',borderwidth=0, command=lambda: random_cheat_screen())

# Variable permettant de savoir si la fonction rainbow mod est activée ou non afin que au premier appuye le mode s'active et au deuxième il s'arrête
Random_color = 1

# Bouton permettant de lancer et d'arrêter le mode 'rainbow' avec une image
Rainbow_img = PhotoImage(file='img\Brainbow_mod_button.png',width=95,height=50)
Bcheat_randomcolor = Button(image=Rainbow_img, bg='#0C343D', activebackground='#0C343D', borderwidth=0, command=lambda: randomcolorcheck())

# Bouton permettant de remttre le highscore à 0
Bclear_highscore = Button(text='Clear Highscore', bg='#0C343D', fg='white',borderwidth=0,command=lambda: clear_highscore())

# Fonction afin de continuer le jeu quand on atteint 2048
def continue_game():
    global Lwin_screen, Bwin, end_game
    Lwin_screen.destroy()
    Bwin.destroy()
    Lwin_screen = Label(image=win_screen,bg='white')
    Bwin = Button(text="Continue", bg='white', fg='black', borderwidth=0, activebackground='white', command=lambda: continue_game(), font=("Ubuntu Mono", 30, "italic"))
    end_game = True
    return end_game

# Fonction qui enlève l'écran de défaite quand on appuye sur afficher le jeu
def loose_game():
    global Lloose_screen, Bloose, end_game2
    Lloose_screen.destroy()
    Bloose.destroy()
    Lloose_screen = Label(image=loose_screen,bg='grey')
    Bloose = Button(bg='grey', fg='black', borderwidth=0, activebackground='grey', text="Afficher le jeu", command=lambda:loose_game(), font=("Ubuntu Mono", 30, "italic"))
    end_game2 = True
    return end_game2

# Fonction pour check si il y a encore un mouvement possible
def check():
    global score
    # Initialiser une variable nomove pour que si il y a un mouvement faisable sur une ligne ou colonne ca ajoute 1 à nomove
    nomove = 0

    # Sauvegarde du score afin que cette fonction n'altère pas le score
    score2 = score

    # Copie de la table afin de ne pas altérer la vraie
    values_tables2 = copy.deepcopy(values_tables)

    # Sauvegarde de la table initiale afin de les comparer
    table_test = copy.deepcopy(values_tables)

    # Tests de toutes les directions possibles voir si un mouvement est possible
    for line in range(4):
        [values_tables2[line][0], values_tables2[line][1], values_tables2[line][2], values_tables2[line][3]] = tasse_4(values_tables2[line][0], values_tables2[line][1], values_tables2[line][2], values_tables2[line][3])
        if [values_tables2[line][0], values_tables2[line][1], values_tables2[line][2], values_tables2[line][3]] == [table_test[line][0], table_test[line][1], table_test[line][2], table_test[line][3]]:
            nomove+=1

        [values_tables2[line][3], values_tables2[line][2], values_tables2[line][1], values_tables2[line][0]] = tasse_4(values_tables2[line][3], values_tables2[line][2], values_tables2[line][1], values_tables2[line][0])
        if [values_tables2[line][3], values_tables2[line][2], values_tables2[line][1], values_tables2[line][0]] == [table_test[line][3], table_test[line][2], table_test[line][1], table_test[line][0]]:
            nomove+=1

        [values_tables2[0][line], values_tables2[1][line], values_tables2[2][line], values_tables2[3][line]] = tasse_4(values_tables2[0][line], values_tables2[1][line], values_tables2[2][line], values_tables2[3][line])
        if [values_tables2[0][line], values_tables2[1][line], values_tables2[2][line], values_tables2[3][line]] == [table_test[0][line], table_test[1][line], table_test[2][line], table_test[3][line]]:
            nomove+=1

        [values_tables2[3][line], values_tables2[2][line], values_tables2[1][line], values_tables2[0][line]] = tasse_4(values_tables2[3][line], values_tables2[2][line], values_tables2[1][line], values_tables2[0][line])
        if [values_tables2[3][line], values_tables2[2][line], values_tables2[1][line], values_tables2[0][line]] == [table_test[3][line], table_test[2][line], table_test[1][line], table_test[0][line]]:
            nomove += 1

    # Si aucun mouvement possible faire apparaître l'écran de fin
    if nomove == 16:
        Lloose_screen.place(x=25,y=110)
        Bloose.place(x=200, y=500)

    # Remettre le score de base
    score = score2

# Fonction afin de mettre les labels à la bonne couleur par rapport à leur couleur est les réafficher si la table à changée
def display(values_table):
    global score,Highscore
    # Augmentation du "Highscore" si le score dépasse le "Highscore"
    if Highscore < score:
        Highscore = score
        text = open("txt\HighScore.txt", "w")
        text.write(str(Highscore))
        text.close()

    for line in range(len(values_tables)):
        for col in range(len(values_tables[line])):

            # Prendre la couleur selon la valeur de la case
            var = values_tables[line][col]
            if var > 8192:
                color = 'black'
            else:
                color = colors[var]
            textcolor = 'white'

            # Changer la couleur de certaine cases pour améliorer la lisibilité
            if var in [2, 4, 64]:
                textcolor = 'black'

            # modifier le text et la couleur des cases
            labels[line][col].config(text=values_tables[line][col], bg=color, fg=textcolor)
            if var == 0:
                labels[line][col].config(text="")

            # vérifier si un 2048  est présent afin d'afficher l'écran de win et demander si il souhaite continuer
            if end_game == False and var == 2048:
                Lwin_screen.place(x=25,y=110)
                Bwin.place(x=400, y=300)

            Lscore.config(text=f"Score : {score}")
            LHighScore.config(text=f'Highscore : {Highscore}')

# Premier affichage de la table
display(values_tables)

# Fonction new game (aide de Thibault)
def newGame():
    global values_tables, score, end_game, end_game2, undo_score

    # Enlever l'écran de victoire (si il a appuyé sur new game avec l'écran de win afficher)
    continue_game()
    end_game = False

    # Enlever l'écran de défaite (si il a appuyé sur new game avec l'écran de loose afficher)
    loose_game()
    end_game2 = False

    # Réinitisaliser le score
    undo_score = score
    score = 0

    # Initialiser un tableau vide
    values_tables = [[0, 0, 0, 0],
                     [0, 0, 0, 0],
                     [0, 0, 0, 0],
                     [0, 0, 0, 0]]

    # Ajoutez une liste afin d'avoir une probabilité de spawn un 4
    spawnable_values = [2, 2, 2, 2, 2, 4]

    # Boucle afin de déterminer deux endroits aléatoires dans le tableau et faire spawn des deux à ces endroits
    for i in range(2):
        x = random.randint(0, 3)
        y = random.randint(0, 3)
        while values_tables[x][y] != 0:
            x = random.randint(0, 3)
            y = random.randint(0, 3)
        values_tables[x][y] = random.choice(spawnable_values)

    # Rappel de la fonction display
    display(values_tables)

# Lancer l'ancienne game si il est existe une
Start_game = open("txt\Gamesave.txt", 'r')
if Start_game.read() != "":
    with open('txt\Gamesave.txt', 'r') as temp_op:
        values_tables = json.load(temp_op)
        undo_table = copy.deepcopy(values_tables)
    display(values_tables)
# Sinon recommencer une nouvelle partie
else:
    newGame()

Start_game.close()

# Recommencer le jeu
Brestart = Button(text='New game',bg='#0C343D',fg='white',borderwidth=0, command=newGame, activebackground='#0C343D').pack()


BUndo.place(x=30, y=30)
Lscore.pack(side=BOTTOM)
LHighScore.pack(side=BOTTOM)
Bcheat.place(x=605, y=780)

# fin app jeu
fen.mainloop()
