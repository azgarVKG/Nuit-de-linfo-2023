import pyxel, math
from random import randint
from mob import aleatoire

class Joueur:
    def __init__(self, pseudo):
        
        #partie pyxel
        self.x = 123
        self.y = 123

        self.score = 0
        self.nb_mauvaise_reponse = 0
        self.nb_bonne_reponse = 0
        self.pv = 5
        self.pvmax = self.pv

        #reponse possible contre un monstre défini en fonction de la fake new du monstre
        self.reponse1 = "aleatoire SQL rep 1"
        self.reponse2 = "aleatoire SQL rep 2"
        self.reponse3 = "aleatoire SQL rep 3"
        self.reponse4 = "aleatoire SQL rep 4"
        self.bonne_reponse = "self.reponse1/2/3/4"


    def victoire(self):
        self.score += 1

    def plus_nb_bonne_reponse(self):
        self.nb_bonne_reponse += 1

    def plus_nb_mauvaise_reponse(self):
        self.nb_mauvaise_reponse += 1
        self.pv -= 1


    #partie pyxel
    def move(self):
        if pyxel.btnp(pyxel.KEY_UP):
            if self.y - 20 > 0:
                self.y -= 20
        if pyxel.btnp(pyxel.KEY_DOWN):
            if self.y + 20 < 256:
                self.y += 20
        if pyxel.btnp(pyxel.KEY_RIGHT):
            if self.x + 20 < 256:
                self.x += 20
        if pyxel.btnp(pyxel.KEY_LEFT):
            if self.x -20 > 0:
                self.x -= 20
