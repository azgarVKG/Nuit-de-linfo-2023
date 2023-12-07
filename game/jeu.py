import pyxel, math
from random import randint

class joueur:
    def __init__(self, pseudo):
        self.score = 0
        self.mauvaise_reponse = 0
        self.bonne_reponse = 0
