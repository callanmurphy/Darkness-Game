# Callan Murphy
# 21/11/19
# Classes File
import pygame
import random
WIDTH = 1276
HEIGHT = 800


class Thing:
    """Parent class for any object on screen"""
    def __init__(self, img, sizex, sizey):
        self.img = pygame.transform.scale(
            pygame.image.load(img).convert_alpha(), (sizex, sizey))
        self.rect = self.img.get_rect()
        self.rect.x = random.randint(sizex, WIDTH-sizex)
        self.rect.y = random.randint(sizey, HEIGHT-sizey)

    def collided(self, obj):
        return self.rect.colliderect(obj)

    def change_img(self, img):
        self.img = pygame.transform.scale(
            pygame.image.load(img).convert_alpha(), (45, 100))

    def collide_fix(self, x):
        # TODO - needs all to be "if" but needs to be fixed
        if self.rect.bottom - 5 < x.rect.top < self.rect.bottom:
            self.rect.y = x.rect.top - self.rect.height
        elif self.rect.top < x.rect.bottom < self.rect.top + 5:
            self.rect.y = x.rect.bottom
        elif x.rect.right > self.rect.x + self.rect.width > x.rect.x:
            self.rect.x = x.rect.x - self.rect.width
        elif x.rect.x < self.rect.x < x.rect.right:
            self.rect.x = x.rect.right

    def collide_top(self, x):
        if self.rect.bottom - 5 < x.rect.top < self.rect.bottom:
            self.rect.y = x.rect.top - self.rect.height

    def collide_bottom(self, x):
        if self.rect.top < x.rect.bottom < self.rect.top + 5:
            self.rect.y = x.rect.bottom

    def collide_right(self, x):
        if x.rect.right > self.rect.x + self.rect.width > x.rect.x:
            self.rect.x = x.rect.x - self.rect.width

    def collide_left(self, x):
        if x.rect.x < self.rect.x < x.rect.right:
            self.rect.x = x.rect.right

    def new_pos(self):
        self.rect.x = random.randint(0, WIDTH)
        self.rect.y = random.randint(0, HEIGHT)
        return self

    def get_position(self):
        return self.rect.x, self.rect.y,

    def check_boundary(self):
        if self.rect.x > WIDTH - self.rect.width:
            self.rect.x = WIDTH - self.rect.width
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.y > HEIGHT - self.rect.height:
            self.rect.y = HEIGHT - self.rect.height
        if self.rect.y < 0:
            self.rect.y = 0


class Mob(Thing):
    """Child class for any onscreen mobs"""
    def __init__(self, name, health, sizex, sizey, img, x=None, y=None):
        Thing.__init__(self, img, sizex, sizey)
        self.name = name
        self.health = health
        # if no x or y provided, random values will be set by parent
        if x is not None and y is not None:
            self.rect.x = x
            self.rect.y = y

    def move_to_obj(self, obj):
        if self.rect.x < obj.rect.x:
            self.rect.x += 1
        if self.rect.x > obj.rect.x:
            self.rect.x -= 1
        if self.rect.y < obj.rect.y:
            self.rect.y += 1
        if self.rect.y > obj.rect.y:
            self.rect.y -= 1


class Barrier(Thing):
    """Child class for any barriers"""
    def __init__(self, img, sizex, sizey):
        Thing.__init__(self, img, sizex, sizey)


class Coin(Thing):
    """Child class for any barriers"""
    def __init__(self, img, sizex, sizey):
        Thing.__init__(self, img, sizex, sizey)
        self.new_pos()

    def new_pos(self):
        self.rect.x = random.randint(0, WIDTH)
        self.rect.y = random.randint(85, HEIGHT)
        return self



