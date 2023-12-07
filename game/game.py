import pyxel 
import random

class Jeu:
    def __init__ (self):
        self.joueur = Joueur()
        self.monster = []
        pyxel.init(256, 256, title="Nom", fps=60, quit_key=pyxel.KEY_ESCAPE )
        pyxel.run(self.update, self.draw)
        pyxel.load("./ndc.pyxres")

    def update (self):
        self.joueur.move()

    def creation_monstre(self):
        for k in range(5):
            self.monster.append(
                {
                    "x":random.randint(0, 256), "y":random.randint(0, 256)
                    }
            )

    def draw(self):
        pyxel.cls(0)
        pyxel.rect(self.joueur.x, self.joueur.y, 10, 10, 3)
        print(self.monster)
        for m in self.monster:
            pyxel.rect(m['x'], m['y'], 10, 10, 7)

class Joueur:
    def __init__(self):
        self.x = 123
        self.y = 123
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

Jeu()