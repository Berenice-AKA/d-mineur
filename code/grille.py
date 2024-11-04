# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 23:32:52 2024

@author: DELL
"""

from random import random
from cellule import Cellule

class Grille:
    def __init__(self, jeu, lignes, colonnes, nombre_mines):
        self.jeu = jeu
        self.lignes = lignes
        self.colonnes = colonnes
        self.nombre_mines = nombre_mines
        self.cellule = [[Cellule(ligne, col) for col in range(self.colonnes)] for ligne in range(self.lignes)]

    def initialiser(self):
        """Initialise les mines et compte les mines voisines pour chaque cellule."""
        mines_placees = 0
        while mines_placees < self.nombre_mines:
            ligne = int(random()*self.lignes)
            col = int(random()*self.colonnes)
            if not self.cellule[ligne][col].est_mine:  
                self.cellule[ligne][col].est_mine = True
                mines_placees += 1
        # Compter les mines voisines pour chaque cellule
        for ligne in range(self.lignes):
            for col in range(self.colonnes):
                self.cellule[ligne][col].mines_voisines = self.compter_mines_voisines(ligne, col)

    def compter_mines_voisines(self, ligne, col):
        """Compte le nombre de mines voisines d'une cellule donnée."""
        voisins = self.obtenir_voisins(ligne, col)
        return sum(1 for cellule in voisins if cellule.est_mine)

    def obtenir_voisins(self, ligne, col):
        """Retourne une liste des cellules voisines."""
        voisins = []
        for l in range(max(0, ligne - 1), min(self.lignes, ligne + 2)):
            for c in range(max(0, col - 1), min(self.colonnes, col + 2)):
                if (l, c) != (ligne, col):
                    voisins.append(self.cellule[l][c])
        return voisins

    def sur_clic_gauche(self, event):
        """Gestion du clic gauche : révéler la cellule cliquée."""
        col = (event.x - 2) // self.jeu.affichage.taille_cellule
        ligne = (event.y - 2) // self.jeu.affichage.taille_cellule
        self.reveler(ligne, col)

    def sur_clic_droit(self, event):
        """Gestion du clic droit : basculer un drapeau sur la cellule cliquée."""
        col = (event.x - 2) // self.jeu.affichage.taille_cellule
        ligne = (event.y - 2) // self.jeu.affichage.taille_cellule
        self.basculer_drapeau(ligne, col)

    def reveler(self, ligne, col):
        cellule = self.cellule[ligne][col]
        if not cellule.est_revelee and not cellule.est_drapeau:
            cellule.reveler()
        # Mettre à jour l'affichage
            if cellule.est_mine:
                return  # Ne rien faire si c'est une mine
            self.jeu.affichage.mettre_a_jour_cellule(ligne, col, "white", str(cellule.mines_voisines) if cellule.mines_voisines > 0 else "")
        
        # Si aucune mine voisine, révéler les cellules adjacentes
            if cellule.mines_voisines == 0:
                for voisin in self.obtenir_voisins(ligne, col):
                    self.reveler(voisin.ligne, voisin.colonne)


    def basculer_drapeau(self, ligne, col):
        """Place ou retire un drapeau sur une cellule et met à jour l'affichage."""
        cellule = self.cellule[ligne][col]
        if not cellule.est_revelee:
            cellule.basculer_drapeau()
            couleur = "orange" if cellule.est_drapeau else "gray"
            self.jeu.affichage.mettre_a_jour_cellule(ligne, col, couleur, "D" if cellule.est_drapeau else None)
        
    def reveler_toutes_les_mines(self):
        """Révèle toutes les mines sur la grille."""
        for ligne in self.cellule:
            for cellule in ligne:
                if cellule.est_mine:
                    cellule.reveler()
                # Mettre à jour l'affichage des mines
                    self.jeu.affichage.mettre_a_jour_cellule(cellule.ligne, cellule.colonne, "red", "M")

