from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import sqlite3



grille = [[
[None,None,None,None,None,None,None,None],
[None,None,None,None,None,None,None,None],
[None,None,None,None,None,None,None,None],
[None,None,None,None,None,None,None,None],
[None,None,None,None,None,None,None,None],
[None,None,None,None,None,None,None,None],
[None,None,None,None,None,None,None,None],
[None,None,None,None,None,None,None,None] ],
[
[None,None,None,None,None,None,None,None],
[None,None,None,None,None,None,None,None],
[None,None,None,None,None,None,None,None],
[None,None,None,None,None,None,None,None],
[None,None,None,None,None,None,None,None],
[None,None,None,None,None,None,None,None],
[None,None,None,None,None,None,None,None],
[None,None,None,None,None,None,None,None] ] ]


def creation_bateau(num_joueur,num_col, li, longueur, num):
    """renvoie la grille avec les numeros des bateaux, et si ya rien bah cest none
    Prend en parametre :
    - num du joueur (0 ou 1) qui definit quelle liste de liste prendre
    - num colonne pour la 1ere sousliste definissant les colonnes
    - li pour la 2e sous liste definissant les lignes
    - longueur qui sera la longueur du bateau
    - num qui correspont a l'etape et au numero du bateau"""
    liste_bateau = []
    if num % 2 == 0 :
        if 7 - num_col >= longueur :
            for i in range(longueur - 1):
                grille[num_joueur][num_col][li] = num
                num_col += 1
        else :
            for i in range(longueur - 1):
                grille[num_joueur][num_col][li] = num
                num_col -= 1
    else :
        if 7 - li >= longueur :
            for i in range(longueur - 1):
                grille[num_col[li]] = num
                li += 1
        else :
            for i in range(longueur - 1):
                grille[num_col[li]] = num
                li -= 1


def nombre_bateaux():
     """Renvoie le nombre de bateaux differents restants """
     bateaux_differents = []
     for i in range(grille):
         for num in i:
             if num not in bateaux_differents:
                 bateaux_differents.append(num)
     return len(bateaux_differents)


def tirer(num_col, li):
    """Retourne si le tir a touche ou non"""
    if grille[num_col[li]] != False and grille[num_col[li]] != None :
         grille[num_col[li]] = False
         return True #en gros c'est touche
    return False #en gros t'es nul t'as rate

def bateau_touche():
    return 0

def vie_bateau(numero):
    """renvoie la vie d'un bateau specifie par son numero entre en parametre"""
    vie_bateau = 0
    for i in grille:
        if i == numero:
            vie_bateau += 1
    return vie_bateau


def reset():
    grille = grille_a_zero


def commencer_tour(joueur_actuel, joueur_prochain):
    """Renvoie une fonction avec comme arguments :
    - le mode
    - la grille de l'adversaire
    - la grille du joueur actuel avec ses bateaux
    - le joueur qui joue
    - le joueur en attente"""
    j1 = joueur_actuel
    j2 = joueur_prochain
    return init_grille(2, "grille adversaire", "grille joueur qui joue (ses bateaux)",j1, j2)