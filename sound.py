# Callan Murphy
# 26/07/20
# Sound File

# from pygame.mixer import *
# pygame.mixer.init()
# pygame.mixer.music.load("music/testsong.wav")
# pygame.mixer.music.play()
from playsound import playsound


def theme_music():
    playsound("music/song1.mp3", False)


def ow():
    playsound("sound/ow.m4a", False)


def coin():
    playsound("sound/coin.m4a", False)
