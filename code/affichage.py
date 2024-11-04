# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 23:43:37 2024

@author: DELL
""" 

from tkinter import Canvas

class Affichage:
    def __init__(self, racine, grille, taille_cellule=15):
        self.canvas = Canvas(racine, width=grille.colonnes * taille_cellule, height=grille.lignes * taille_cellule, bg="white")
        self.canvas.pack()
        self.grille = grille
        self.taille_cellule = taille_cellule

        # Création des cellules visuelles et des textes pour chaque cellule
        self.cellules_visuelles = [[self.creer_cellule_visuelle(ligne, col) for col in range(grille.colonnes)] for ligne in range(grille.lignes)]
        self.textes_visuels = [[None for _ in range(grille.colonnes)] for _ in range(grille.lignes)]
        
    def reinitialiser(self, racine, grille, taille_cellule=15):
        self.canvas.pack_forget()
        self.canvas = Canvas(racine, width=grille.colonnes * taille_cellule, height=grille.lignes * taille_cellule, bg="white")
        self.canvas.pack()
        self.grille = grille
        self.taille_cellule = taille_cellule

        # Création des cellules visuelles et des textes pour chaque cellule
        self.cellules_visuelles = [[self.creer_cellule_visuelle(ligne, col) for col in range(grille.colonnes)] for ligne in range(grille.lignes)]
        self.textes_visuels = [[None for _ in range(grille.colonnes)] for _ in range(grille.lignes)]

    def creer_cellule_visuelle(self, ligne, col):
        x1 = col * self.taille_cellule
        y1 = ligne * self.taille_cellule
        x2 = x1 + self.taille_cellule
        y2 = y1 + self.taille_cellule
        return self.canvas.create_rectangle(x1, y1, x2, y2, outline="black", fill="gray")

    def mettre_a_jour_cellule(self, ligne, col, couleur, texte=None):
        cellule_visuelle = self.cellules_visuelles[ligne][col]
        self.canvas.itemconfig(cellule_visuelle, fill=couleur)
        
        # Mettre à jour ou créer le texte associé à la cellule
        if texte:
            if self.textes_visuels[ligne][col] is not None:
                # Mettre à jour le texte existant
                self.canvas.itemconfig(self.textes_visuels[ligne][col], text=texte)
            else:
                # Créer le texte si non existant
                x = col * self.taille_cellule + self.taille_cellule // 2
                y = ligne * self.taille_cellule + self.taille_cellule // 2
                self.textes_visuels[ligne][col] = self.canvas.create_text(x, y, text=texte)
        elif self.textes_visuels[ligne][col] is not None:
            self.canvas.delete(self.textes_visuels[ligne][col])
            self.textes_visuels[ligne][col] = None

