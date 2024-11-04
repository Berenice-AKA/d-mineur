# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 23:32:52 2024

@author: DELL
"""


from tkinter import Tk, Label,simpledialog,messagebox,Menu
from affichage import Affichage
from grille import Grille
from chronometre import Chronometre

class Jeu:
    def __init__(self):
        self.root = Tk()
        self.root.title("Démineur")
        
        self.menu = Menu(self.root)
        self.root.config(menu=self.menu)
       
        self.nouvelle_partie_menu = Menu(self.menu)
        self.menu.add_cascade(label="Partie", menu=self.nouvelle_partie_menu)
        self.nouvelle_partie_menu.add_command(label="Nouvelle Partie", command=self.nouvelle_partie)
        # Demande de sélection de la difficulté
        self.difficulte = simpledialog.askstring("Difficulté", "Choisissez un niveau (facile, moyen, difficile):")
        
        if self.difficulte == "facile":  
            self.lignes = 10
            self.colonnes = 10
            self.nombre_mines = 10
        elif self.difficulte == "moyen":  
            self.lignes = 16
            self.colonnes = 16
            self.nombre_mines = 20
        elif self.difficulte == "difficile":  
            self.lignes = 24
            self.colonnes = 24
            self.nombre_mines = 40
        else:
            raise ValueError("Niveau de difficulté invalide")
        
        self.chronometre = Chronometre()  # Instancier le chronomètre
        self.chronometre.commencer()       # Commencer le chronomètre
        
        
        self.label_temps = Label(self.root, text="Temps : 0")  # Label pour afficher le temps
        self.label_temps.pack()
        
        
        self.grille = Grille(self,self.lignes, self.colonnes, self.nombre_mines)
        self.affichage = Affichage(self.root, self.grille)
        
        # Liaison des clics gauche et droit aux fonctions du jeu
        self.affichage.canvas.bind("<Button-1>", self.sur_clic_gauche)
        self.affichage.canvas.bind("<Button-3>", self.grille.sur_clic_droit)
        
        self.jeu_termine = False
         

        
        
    def nouvelle_partie(self):
        """Réinitialise le jeu pour une nouvelle partie."""
        self.chronometre.arreter()  # Arrêter le chronomètre si actif
         
        self.chronometre = Chronometre()  # Créer un nouveau chronomètre
        self.chronometre.commencer()  # Commencer le chronomètre

       # Mettre à jour le temps
        self.label_temps.config(text="Temps : 0")
       
      # Demander de nouveau la difficulté
        self.difficulte = simpledialog.askstring("Difficulté", "Choisissez un niveau (facile, moyen, difficile):")
        if self.difficulte == "facile": 
            self.lignes = 10
            self.colonnes = 10
            self.nombre_mines = 10
        elif self.difficulte == "moyen":  
            self.lignes = 16
            self.colonnes = 16
            self.nombre_mines = 20
        elif self.difficulte == "difficile":  
            self.lignes = 24
            self.colonnes = 24
            self.nombre_mines = 40
        else:
            raise ValueError("Niveau de difficulté invalide")

        # Créer une nouvelle grille et affichage
        self.grille = Grille(self, self.lignes, self.colonnes, self.nombre_mines)
        self.grille.initialiser()
        self.affichage.reinitialiser(self.root, self.grille)
        self.affichage.canvas.bind("<Button-1>", self.sur_clic_gauche)
        self.affichage.canvas.bind("<Button-3>", self.grille.sur_clic_droit)

 
        
    def sur_clic_gauche(self, event):
        if not self.jeu_termine:  
            self.grille.sur_clic_gauche(event)
            col = (event.x - 2) // self.affichage.taille_cellule
            ligne = (event.y - 2) // self.affichage.taille_cellule
        
        # Vérifier si la cellule révélée est une mine
            if self.grille.cellule[ligne][col].est_mine:
                self.grille.reveler_toutes_les_mines()  # Révéler toutes les mines
                self.afficher_message("Dommage vous avez perdu", self.chronometre.afficher_temps())
                self.jeu_termine = True  
            else:
                if self.verifier_victoire():
                    self.afficher_message("Félicitations vous avez gagné", self.chronometre.afficher_temps())
                    self.jeu_termine = True  


    def afficher_message(self, resultat, temps):
        """Affiche un message de résultat avec le temps écoulé."""
        message = f"{resultat}! Temps écoulé : {temps} secondes."
        messagebox.showinfo("Fin du jeu", message)
        self.finir()   

    def verifier_victoire(self):
        """Vérifie si toutes les cellules non-mines sont révélées pour déterminer la victoire."""
        for ligne in self.grille.cellule:
            for cellule in ligne:
                if not cellule.est_mine and not cellule.est_revelee:
                    return False
        return True


    def afficher_toutes_les_mines(self):
        """Affiche toutes les mines à la fin de la partie pour révéler leur emplacement."""
        for ligne in self.grille.cellule:
            for cellule in ligne:
                if cellule.est_mine:
                    self.affichage.mettre_a_jour_cellule(cellule.ligne, cellule.colonne, couleur="red", texte="M")

    def finir(self):
        """Arrête le chronomètre et affiche le temps écoulé."""
        self.chronometre.arreter()
        temps = self.chronometre.afficher_temps()
        print(f"Temps écoulé : {temps}")
    
    def mettre_a_jour_affichage(self):
        """Met à jour l'affichage du temps chaque seconde."""
        temps = self.chronometre.afficher_temps()
        self.label_temps.config(text=f"Temps : {temps}")   
        self.root.after(1000, self.mettre_a_jour_affichage)  # Mettre à jour chaque seconde

    def demarrer(self):
        """Démarre le jeu et initialise la grille."""
        self.grille.initialiser()
        self.mettre_a_jour_affichage()  
        self.root.mainloop()

if __name__ == "__main__":
    jeu = Jeu()
    jeu.demarrer()
