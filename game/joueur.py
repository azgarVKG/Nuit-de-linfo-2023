import pyxel, math
from random import randint

class Joueur:
    def __init__(self, pseudo):
        self.score = 0
        self.mauvaise_reponse = 0
        self.bonne_reponse = 0
        self.pv = 5
        self.pvmax = self.pv

    def victoire(self):
        self.score += 1

    def bonne_reponse(self):
        self.bonne_reponse += 1

    def mauvaise_reponse(self):
        self.mauvaise_reponse += 1
        self.pv -= 1

