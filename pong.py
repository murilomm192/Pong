import pygame
from constants import *

pygame.init()
screen = pygame.display.set_mode(screenLargura, ScreenAltura)

class Ball:
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed

class Player:
    def __init__(self, x, y, altura, largura, speed):
        self.x = x
        self.y = y
        self.altura = altura
        self.largura = largura
        self.speed = speed


def screen_update():
    #tudo que deve ser desenhado entra nessa função
    screen.blit(BLACK)
    pygame.display.update()

#gameloop
loop = True
while loop:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        loop = False
        
        screen_update()
