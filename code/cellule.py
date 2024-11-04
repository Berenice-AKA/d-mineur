# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 23:34:57 2024

@author: DELL
"""

class Cellule:
    def __init__(self, ligne, colonne):
        self.ligne = ligne
        self.colonne = colonne
        self.est_mine = False
        self.est_revelee = False
        self.est_drapeau = False
        self.mines_voisines = 0

    def reveler(self):
        """Révèle la cellule si elle n'est pas déjà révélée ou marquée d'un drapeau."""
        if not self.est_revelee and not self.est_drapeau:
            self.est_revelee = True
            if self.est_mine:
                print("Boom! Mine révélée.")
            else:
                print(f"Nombre de mines voisines: {self.mines_voisines}")

    def basculer_drapeau(self):
        """Active ou désactive le drapeau sur la cellule."""
        if not self.est_revelee:  # On ne peut pas mettre de drapeau sur une case révélée
            self.est_drapeau = not self.est_drapeau

    def definir_comme_mine(self):
        """Définit la cellule comme une mine."""
        self.est_mine = True

    def definir_mines_voisines(self, nombre):
        """Définit le nombre de mines dans les cellules voisines."""
        self.mines_voisines = nombre

    def get_nombre_mines_autour(self):
        """Retourne le nombre de mines dans les cellules voisines."""
        return self.mines_voisines

