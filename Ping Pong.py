from pygame import *
from time import time as timer
import random
window = display.set_mode((700,500))
display.set_caption("Ping Pong")
backgr = transform.scale(image.load('table.png'), (700,500))
window.blit(backgr,(0,0))


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
font.init()
font = font.SysFont('Arial', 70)


class Ball(GameSprite):
    pass


spr1 = Player('racket.png', 0, 400, 7, 80, 110)
spr2 = Player2('racket.png', 600, 400, 7, 80, 110)
spr3 = Ball('ball.png', 250, 350, 3, 80, 50)




# clock = time.Clock()
# x1 = 0
# y1 = 450
# x2 = 650
# y2 = 300
# FPS = 60
# speed = 10
# chet = 0
game = True
finish = False
speed_x = 2
speed_y = 2


# win = font.render('YOU WIN!', True, (255,215,0))
# lose = font.render('YOU LOSE!', True, (255,215,0))

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
        # if spr3.rect.x < 0 or spr3.rect.x > 700:
        #     print('sdfsdf')     

        spr1.update()
        spr1.reset()


        spr2.update()
        spr2.reset()

        spr3.update()
        spr3.reset()


    display.update()
    