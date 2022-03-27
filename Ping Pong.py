from pygame import *
from time import time as timer
import random
window = display.set_mode((700,500))
display.set_caption("shooter game")
backgr = transform.scale(image.load('galaxy.jpg'), (700,500))
window.blit(backgr,(0,0))

num_fire = 5
rel_time = False
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
        if keys_pressed[K_d] and self.rect.x < 650:
            self.rect.x += self.speed
        if keys_pressed[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
    def fire(self):
        spr7 = Bullet('bullet.png', self.rect.centerx, self.rect.top,5,20, 20)
        bullets.add(spr7)
lost = 0
font.init()
font = font.SysFont('Arial', 70)
class Enemy(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed, width, height):
        self.direction = 'down'
        self.y2 = 500
        self.y1 = 0
        super().__init__(player_image, player_x, player_y, player_speed, width, height)
    def update(self): 
        self.rect.y += self.speed  
        global lost    
        if self.rect.y >= self.y2:
            self.rect.y = 0
            self.rect.x = random.randint(0, 700)
            lost = lost + 1

class Bullet(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed, width, height):
        self.direction = 'up'
        self.y2 = 500
        self.y1 = 0
        super().__init__(player_image, player_x, player_y, player_speed, width, height)
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y <= self.y1:          
            self.kill()
lost2 = 5

class Asteroid(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed, width, height):
        self.direction = 'down'
        self.y2 = 500
        self.y1 = 0
        super().__init__(player_image, player_x, player_y, player_speed, width, height)
    def update(self): 
        self.rect.y += self.speed  
        global lost2   
        if self.rect.y >= self.y2:
            self.rect.y = 0
            self.rect.x = random.randint(0, 700)

spr1 = Player('rocket.png', 0, 400, 7, 70, 100)
spr2 = Enemy('ufo.png', 202, 2, 2, 100, 70)
spr3 = Enemy('ufo.png', 550, 10, 3, 90, 60)
spr4 = Enemy('ufo.png', 400, 2, 3, 90,60)
spr5 = Enemy('ufo.png', 600, 15, 4, 70, 50)
spr6 = Enemy('ufo.png', 100, 90, 1, 120,80)
spr9 = Asteroid('asteroid.png', 550, 10, 3, 90 ,60)

monsters = sprite.Group()
monsters.add(spr2,spr3,spr4,spr5,spr6)
bullets = sprite.Group()

asteroids = sprite.Group()
asteroids.add(spr9)

players = sprite.Group()
players.add(spr1)

clock = time.Clock()
x1 = 0
y1 = 450
x2 = 650
y2 = 300
FPS = 60
speed = 10
chet = 0
game = True
finish = False
 

win = font.render('YOU WIN!', True, (255,215,0))
lose = font.render('YOU LOSE!', True, (255,215,0))
last_time = timer()
now_time = timer()
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                print(num_fire)
                if num_fire <= 5 and num_fire > 0:
                    spr1.fire()
                    num_fire -= 1
                 
                if rel_time == False and num_fire == 0:
                    rel_time = True
                    now_time = timer()

    if finish != True:
        window.blit(backgr,(0,0))
        
        text_win = font.render("Счет: " + str(chet), 1, (255,255,255))
        text_chet = font.render(str(lost2), 1, (255,0,0))
        chet_bullet = font.render(str(num_fire), 1, (255,255,0))
        monsters.draw(window)
        asteroids.draw(window)
        bullets.draw(window)
        monsters.update()
        bullets.update()
        spr1.reset()
        asteroids.update()
        spr1.update()
        clock.tick(FPS)
        window.blit(text_win, (0,50))
        window.blit(text_chet, (650, 0))
        window.blit(chet_bullet, (50, 450))
        if rel_time == True:   
            if timer() - now_time < 2:
                text_bullet = font.render("Wait, reload... ", 1, (255,100,100))
                window.blit(text_bullet, (200,400))   
            else:
                num_fire = 5
                rel_time = False

                    
        if sprite.groupcollide(monsters, bullets, True, True):
            spr8 = Enemy('ufo.png', random.randint(0, 700), 0, random.randint(1,3), 120,80)
            monsters.add(spr8)      
            chet += 1
        
        if sprite.groupcollide(players, asteroids, False, True):
            spr9 = Asteroid('asteroid.png', random.randint(0, 700), 0, random.randint(1,5), 90,60)
            asteroids.add(spr9)
            lost2 -= 1

        keys_pressed = key.get_pressed()
        if lost >= 15:
            window.blit(lose, (200,200))
            finish = True
        if chet >= 5:
            window.blit(win, (200, 200))
            finish = True
        if lost2 <= 0:
            window.blit(lose, (200, 200))
            finish = True
            
        text_lose = font.render("Пропущено: " + str(lost), 1, (255,255,255))
        window.blit(text_lose, (0,0))

        text_win = font.render("Счет: " + str(chet), 1, (255,255,255))
        window.blit(text_win, (0,50))

        text_chet = font.render(str(lost2), 1, (255,0,0))
        window.blit(text_chet, (650, 0))

        chet_bullet = font.render(str(num_fire), 1, (255,255,0))
        window.blit(chet_bullet, (50, 450))


    display.update()
    