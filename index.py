from tkinter import *
from tkinter import ttk 
import sqlite3
from random import random


grille = [[
[None,None,None,None,None,None,None,None],
[None,None,None,None,None,None,None,None],
[None,None,None,None,None,None,None,None],
[None,None,None,None,None,None,None,None],
[None,None,None,None,None,None,None,None],
[None,None,None,None,None,None,None,None],
[None,None,None,None,None,None,None,None],
[None,None,None,None,None,None,None,None] ]
[
[None,None,None,None,None,None,None,None],
[None,None,None,None,None,None,None,None],
[None,None,None,None,None,None,None,None],
[None,None,None,None,None,None,None,None],
[None,None,None,None,None,None,None,None],
[None,None,None,None,None,None,None,None],
[None,None,None,None,None,None,None,None],
[None,None,None,None,None,None,None,None] ]]


def longueur_bateau():
    """pour savoir la longueur des bateaux"""
    L_j0 = []
    for i in range(6):
        n = random(1,3)
        L_j0.append(n)
    L_j1 = L_j0
    return L_j0 , L_j1

def select_joueur():
    selectIn = sqlite3.connect('general.db')
    cursor = selectIn.cursor()
    cursor.execute("SELECT nom FROM joueurs")
    player_names = [row[0] for row in cursor.fetchall()]
    selectIn.close()

def changement_de_joueur(joueur):
    return 

def tirer(num_col, li):
    if grille[num_col[li]] != False and grille[num_col[li]] != None :
         grille[num_col[li]] = False
         return True #en gros c'est touche
    return False #en gros t'es nul t'as rate


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