import pygame
from constants import *

pygame.init()
screen = pygame.display.set_mode((screenLargura, screenAltura))
pygame.display.set_caption("Python Pong")
bola_sprite = pygame.image.load('bola.png')

class Ball:
    def __init__(self, x, y, r, speedx,speedy):
        self.x = x
        self.y = y
        self.r = r
        self.speedx = speedx
        self.speedy = speedy

    def draw_Ball(self):
        screen.blit(bola_sprite,(self.x,self.y))

    def move_Ball(self):
        self.x += self.speedx
        self.y += self.speedy
        if self.y + 26 > screenAltura or self.y < 0:
                self.speedy = -self.speedy
        if self.x + 26 > screenLargura or self.x < 0:
                self.speedx = -self.speedx
        if self.x == 30  and self.y+13 > player1.y and self.y+13 < player1.y+50:
                self.speedx = -self.speedx
        if self.x + 26 > 570 and self.y+13 > player2.y and self.y+13 < player2.y+50:
                self.speedx = -self.speedx


class Player:
    def __init__(self, x, y, altura, largura, speed):
        self.x = x
        self.y = y
        self.altura = altura
        self.largura = largura
        self.speed = speed

    def player_move(self):
        if keys[pygame.K_UP] and self.y > self.speed:
                self.y -= self.speed
        if keys[pygame.K_DOWN] and self.y + self.speed < screenAltura - self.largura:
                self.y += self.speed
    
    def draw_Player(self):
        pygame.draw.rect(screen,WHITE,(self.x, self.y, self.altura, self.largura))

class AI:
    def __init__(self, x, y, altura, largura, speed):
        self.x = x
        self.y = y
        self.altura = altura
        self.largura = largura
        self.speed = speed

    def AI_move(self):
        if self.y < bola.y:
                self.y += self.speed 
        if self.y + 25 > bola.y:
                self.y -= self.speed 
    
    def AI_draw(self):
        pygame.draw.rect(screen,RED,(self.x, self.y, self.altura, self.largura))

#criar os objetos:
player1 = Player(10,screenAltura/2-25,20,50,7)
bola = Ball(300,200,10,5,5)
player2 = AI(screenLargura-30,screenAltura/2-25,20,50,7)




def screen_update():
    #tudo que deve ser desenhado entra nessa função
    screen.fill(BLACK)
    player1.draw_Player()
    player2.AI_draw()
    bola.draw_Ball()
    pygame.display.update()

#gameloop
loop = True
while loop:
        pygame.time.Clock().tick(60)
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        loop = False
        
        keys = pygame.key.get_pressed()

        player1.player_move()
        player2.AI_move()
        bola.move_Ball()        
        screen_update()
