from pygame import *
from time import time as timer
import random
window = display.set_mode((700,500))
display.set_caption("Ping Pong")
backgr = transform.scale(image.load('table.png'), (700,500))
window.blit(backgr,(0,0))

font.init()
font = font.SysFont('Arial', 50)

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, width, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (width, height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_s] and self.rect.y < 415:
            self.rect.y += self.speed
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
class Player2(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_DOWN] and self.rect.y < 415:
            self.rect.y += self.speed
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed



class Ball(GameSprite):
    pass


spr1 = Player('racket.png', 0, 400, 7, 80, 110)
spr2 = Player2('racket.png', 600, 400, 7, 80, 110)
spr3 = Ball('ball.png', 250, 350, 3, 80, 50)

chet1 = 0
chet2 = 0
game = True
finish = False
speed_x = 2
speed_y = 2


win = font.render('Игрок справа выиграл!', True, (255,215,0))
lose = font.render('Игрок слева выиграл!', True, (255,215,0))
center = font.render(':', True, (100,100,100))
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        window.blit(backgr,(0,0))
        spr3.rect.x += speed_x
        spr3.rect.y += speed_y
        if spr3.rect.y <= 0 or spr3.rect.y >= 460:
            speed_y *= -1
        
        if sprite.collide_rect(spr1, spr3) or sprite.collide_rect(spr2, spr3):
            speed_x *= -1
        if chet1 == 0:
            window.blit(center, (330, 0))
        if spr3.rect.x <= -70:
            chet1 += 1
            print(chet1)
            spr3.rect.x = 300
            speed_x *= -1

        if spr3.rect.x >= 700:
            chet2 += 1
            print(chet2)
            spr3.rect.x = 300
            speed_x *= -1


        if chet1 >= 5:
            window.blit(win, (-1,50))
            finish = True
        if chet2 >= 5:
            window.blit(lose, (-1,50))
            finish = True
        chet_right = font.render(str(chet1), 1, (100,100,100))
        window.blit(chet_right, (350,0))

        

        chet_left = font.render(str(chet2), 1, (100,100,100))
        window.blit(chet_left, (300,0))

        spr1.update()
        spr1.reset()


        spr2.update()
        spr2.reset()

        spr3.update()
        spr3.reset()


    display.update()