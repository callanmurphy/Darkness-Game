# Callan Murphy
# 21/11/19
# Functions File
from classes import *


def create(obj, amount):
    """Creates <amount> of <obj> and returns list of them"""
    lst = []

    # creation
    for i in range(amount):
        if obj == "wall":
            if random.randint(0, 1) == 1:
                x = Barrier("img/wall.png", random.randint(50, 70),
                            random.randint(100, 200))
            else:
                x = Barrier("img/wall.png", random.randint(100, 200),
                            random.randint(50, 70))
        elif obj == "skele":
            x = Mob("Skele", 50, 45, 100, "img/skele.png")
        elif obj == "coin":
            x = Coin("img/coin.png", 25, 25)
        else:
            return []
        lst.append(x)

    return lst


def fix_spawns(lst):
    for x in lst:
        total = 0
        while total != len(lst) - 1:
            total = 0
            for y in lst:
                if x != y:
                    if x.collided(y):
                        x.new_pos()
                    else:
                        total += 1
    return lst


def fix_collisions(lst):
    for x in lst:
        for y in lst:
            if y.collided(x):
                y.collide_fix(x)
    return lst
