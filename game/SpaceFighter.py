import pyxel, math
from random import randint

liste_tir, liste_ennemi, liste_boss, settings = [], [], [], [1]
x, y, cooldown, niveau, kill, bosscount = 100, 240, 1, 1, 0, 50
jeu, vie = False, True

def parametre(settings:list[int]) -> list[int]:
    """
    Gère les paramètres du jeu avant le début de la partie
    """
    if not jeu:
        if pyxel.btnp(pyxel.KEY_UP) and settings[0] != 3:
            settings[0] +=1
        if pyxel.btnp(pyxel.KEY_DOWN) and settings[0] != 1:
           settings[0] -= 1
    return settings

def menu() -> bool:
    """
    Gère le menu du jeu
    """
    if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
        return True
    return False

def deplacement_perso(x:int, y:int) -> int:
    """
    Permet de mettre en place les mouvements du vaisseaux
    """
    if pyxel.btnp(pyxel.KEY_RIGHT, 1, 1) and x!= 190:
        x += 1
    if pyxel.btnp(pyxel.KEY_LEFT, 1, 1) and x!= 0:
        x -= 1
    if pyxel.btnp(pyxel.KEY_UP, 1, 1) and y!= 0:
        y -= 1
    if pyxel.btnp(pyxel.KEY_DOWN, 1, 1) and y!= 260:
        y += 1
    return x, y

def spawn_tir(liste_tir:list[list[int]], x:int, y:int, cooldown: int) -> list[list[int]]:
    """
    Permet de tirer avec espace (système de cooldown)
    """
    if (pyxel.frame_count % 30 == 0):
        cooldown = 1
    if pyxel.btnp(pyxel.KEY_SPACE, 1, 1) and cooldown == 1:
        liste_tir.append([x+4, y-4])
        pyxel.play(0,0)
        cooldown = 0
    return liste_tir, cooldown

def tir_deplacement(liste_tir: list[list[int]])-> list[list[int]]:
    """
    Gère le déplacement des tirs
    """
    for tir in liste_tir:
        tir[1] -= 1
        if tir[1] == 0:
            liste_tir.remove(tir)
        if len(liste_tir) <= 0:
            return []
    return liste_tir

def spawn_ennemi(liste_ennemi: list[list[int]]) -> list[list[int]]:
    """
    Gère le spawn des ennemis (toutes les 60 frames)
    """
    if (pyxel.frame_count % int((360/niveau+(2/settings[0]))) == 0):
        liste_ennemi.append([randint(20, 180), 0])
    return liste_ennemi

def ennemi_deplacement(liste_ennemi:list[list[int]]) ->  list[list[int]]:
    """
    Gère le mouvement des ennemis (phase roam -> phase target)
    """
    for ennemi in liste_ennemi:
        if ennemi[1] < y-120:
            ennemi[0] += randint(-1, 1)
        else:
            if ennemi[0]-x < 0:
                ennemi[0]+= 1
            else:
                ennemi[0]-= 1
        if ennemi[1] > y:
            ennemi[1] -= 1
        else:
            ennemi[1] += 1
    return liste_ennemi

def touche(kill: int) -> int:
    """
    Gère la collision tir // ennemi
    """
    for ennemi in liste_ennemi:
        for tir in liste_tir:
            if ennemi[0] <= tir[0]+10 and ennemi[1] <= tir[1]+10 and ennemi[0]+10 >= tir[0] and ennemi[1]+10 >= tir[1]:
                if ennemi in liste_ennemi:
                    liste_ennemi.remove(ennemi)
                    liste_tir.remove(tir)
                    pyxel.play(2,2)
                    kill += 1
    for boss in liste_boss:
        for tir in liste_tir:
            if boss[0] <= tir[0]+10 and boss[1] <= tir[1]+10 and boss[0]+50 >= tir[0] and boss[1]+50 >= tir[1]:
                if boss in liste_boss:
                    boss[2] -= 1
                    liste_tir.remove(tir)
                    pyxel.play(2,2)
                    if boss[2] == 0:
                        liste_boss.remove(boss)
                        kill += 1
    return kill

def joueur_touche(vie:bool) -> int:
    """
    Gère la collision joueur // ennemi
    """
    for ennemi in liste_ennemi:
        if ennemi[0] <= x+10 and ennemi[1] <= y+10 and ennemi[0]+10 >= x and ennemi[1]+10 >= y:
            if ennemi in liste_ennemi:
                liste_ennemi.remove(ennemi)
                vie = False
                pyxel.play(1,1)
    for boss in liste_boss:
        if boss[0] <= x+10 and boss[1] <= y+10 and boss[0]+50 >= x and boss[1]+50 >= y:
            if boss in liste_boss:
                liste_boss.remove(boss)
                vie = False
                pyxel.play(1,1)
    return vie

def gestion_niveau(niveau: int, kill:int) ->int:
    """
    Gère le nombre de niveau
    """
    niveau = int(math.sqrt(kill)) + 1
    return niveau

def spawn_boss(kill:int, bosscount: int) -> int:
    """
    Gère le spawn de boss
    """
    if kill == bosscount:
        bosscount+= 50
        liste_boss.append([75, 0, 7])
    return liste_boss, bosscount

def boss_deplacement(liste_boss:list[list[int]]) -> list[list[int]]:
    """
    Gère le déplacement des boss
    """
    for boss in liste_boss:
        if boss[1] < y-120:
            boss[0] += randint(-1, 1)
        else:
            if boss[0]-x < 0:
                boss[0]+= 1
            else:
                boss[0]-= 1
        if boss[1] > y:
            boss[1] -= 1
        else:
            boss[1] += 1
    return liste_boss

def respawn_menu(x:int, y:int, liste_tir: list[list[int]], liste_ennemi:list[list[int]], liste_boss:list[list[int]], cooldown:int, vie:bool, niveau:int, kill:int, bosscount:int):
    """
    Gère l'option pour rejouer
    """
    if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
        x, y= 100, 240
        liste_tir, liste_ennemi, liste_boss = [], [], []
        cooldown, vie, niveau = 1, True, 1
        kill, bosscount = 0, 50
    return x, y, liste_tir, liste_ennemi, liste_boss, cooldown, vie, niveau, kill, bosscount
        
def update():
    global x, y, liste_tir, liste_ennemi, liste_boss, cooldown, vie, niveau, kill, bosscount, jeu, settings

    if not jeu:
        # Gère le menu du jeu
        jeu = menu()

        # Gère les paramètres du jeu avant le début de la partie
        settings = parametre(settings)

    if vie and jeu:
        #Permet de mettre en place les mouvements du vaisseaux
        x,y = deplacement_perso(x,y)

        #Permet de créé les tirs
        liste_tir, cooldown = spawn_tir(liste_tir, x, y, cooldown)

        #Gère le déplacement des tirs
        liste_tir = tir_deplacement(liste_tir)

        if len(liste_boss) == 0:
            #Gère le spawn des ennemis
            liste_ennemi= spawn_ennemi(liste_ennemi)

        #Gère le déplacement des ennemis
        liste_ennemi= ennemi_deplacement(liste_ennemi)

        # Regarde si un tir touche un ennemi
        kill = touche(kill)

        # Regarde si un ennemi a touché le joueur
        vie = joueur_touche(vie)

        # Gère le système de niveau
        niveau = gestion_niveau(niveau, kill)

        # Gère le spawn de boss
        liste_boss, bosscount = spawn_boss(kill, bosscount)

        # Gère le déplacement des boss
        liste_boss = boss_deplacement(liste_boss)

    if not vie:
        # Gère l'option pour rejouer
        x, y, liste_tir, liste_ennemi, liste_boss, cooldown, vie, niveau, kill, bosscount = respawn_menu(x, y, liste_tir, liste_ennemi, liste_boss, cooldown, vie, niveau, kill, bosscount)

def draw():
    pyxel.cls(0)
    pyxel.text(5, 275, f"Niveau : {niveau}", 7)
    pyxel.text(155, 275, f"Kills : {kill}", 7)
    pyxel.line(0, 270, 200, 270, 7)
    if not jeu:
        pyxel.mouse(True)
        pyxel.text(60, 10, "Click here to play!", 3)
        pyxel.text(2, 20, "Fleches Directionnelles : Bouger / Espace : Tirer", 3)
        pyxel.text(10, 70, f"Fleches Hauts/Bas - Changer difficulte: {settings[0]}/3", 3)
    else:
        pyxel.mouse(False)
    if not vie:
        pyxel.text(70, 120, "YOU ARE DEAD !", 3)
        pyxel.text(55, 140, "Click here to respawn", 3)
        pyxel.mouse(True)
    if vie:
        pyxel.blt(x, y, 0, 3, 5, 10, 10)
        for boss in liste_boss:
            pyxel.text(boss[0] + 13, boss[1] - 5, f"Vie: {boss[2]}", 7)
            pyxel.blt(boss[0], boss[1], 1, 0, 0, 50, 50)
        for tir in liste_tir:
            pyxel.rect(tir[0], tir[1], 1, 4, 10)
        for ennemi in liste_ennemi:
            pyxel.blt(ennemi[0], ennemi[1], 0, 19, 3, 10, 10)
    for i in range(10):
        x1= randint(10, 190)
        y1= randint(10, 260,)
        pyxel.line(x1, y1, x1, y1, 7)

pyxel.init(200, 285, "SpaceFighter", 60, pyxel.KEY_ESCAPE)
pyxel.load("my_resource.pyxres")
pyxel.run(update, draw)