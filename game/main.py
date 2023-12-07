import pyxel, math
from joueur import Joueur

class Jeu:
    def __init__(self):

        #ârtie Noé Pyxel
        self.joueur = Joueur()
        pyxel.init(256, 256, title="Nom", fps=60, quit_key=pyxel.KEY_ESCAPE )
        pyxel.run(self.update, self.draw)
        pyxel.load("./ndc.pyxres")

    #partie Pyxel
    def update (self):
        self.joueur.move()
    #partie pyxel
    def draw(self):
        pyxel.cls(0)
        pyxel.rect(self.joueur.x, self.joueur.y, 10, 10, 3)
        pyxel.bltm(0, 0, 0, 0, 0, 15, 15)