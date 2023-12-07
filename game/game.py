import pyxel, json

class App:
    def __init__(self):
        self.x = 0
        pyxel.init(160, 120, title="Name", fps=60, quit_key=pyxel.KEY_ESCAPE)
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_SPACE):
            with open("data.json", "r") as file:
                data = json.load(file)
                data["click"] += 1
            with open("data.json", "w") as file:
                json.dump(data, file)
        if pyxel.btnp(pyxel.KEY_A):
            pyxel.quit()
        if pyxel.btnp(pyxel.KEY_Z):
            self.x += 1

    def draw(self):
        pyxel.rect(self.x, 0, 10, 10, 5)
        pyxel.cls(0)

App()