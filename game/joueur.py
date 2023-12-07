import pyxel, math
from random import randint

class Joueur:
    def __init__(self, pseudo):
        
        #partie pyxel
        self.x = 123
        self.y = 123

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
