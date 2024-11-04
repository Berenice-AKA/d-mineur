# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 00:18:20 2024

@author: DELL
"""

import time

class Chronometre:
    def __init__(self):
        self.temps_debut = None
        self.temps_ecoule = 0

    def commencer(self):
        self.temps_debut = time.time()

    def arreter(self):
        if self.temps_debut is not None:
            self.temps_ecoule += time.time() - self.temps_debut
            self.temps_debut = None

    def reset(self):
        self.temps_ecoule = 0
        self.temps_debut = None

    def obtenir_temps(self):
        if self.temps_debut is not None:
            return self.temps_ecoule + (time.time() - self.temps_debut)
        return self.temps_ecoule

    def afficher_temps(self):
        temps = self.obtenir_temps()
        minutes, secondes = divmod(int(temps), 60)
        return f"{minutes:02}:{secondes:02}"  # Format MM:SS
