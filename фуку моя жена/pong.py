
from pygame import *
from random import *
mixer.init()

window = display.set_mode((700, 500))
display.set_caption('что...')

background = transform.scale(image.load('black.jpg'), (700, 500))
mixer.music.load('Mylène Farmer - Lamour nest rien.mp3')
mixer.music.play()
clock = time.Clock()
FPS = 60


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, shirina, visota):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (shirina, visota))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))
    
class Player(GameSprite):      
    def walk(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 400:
            self.rect.y += self.speed

class PlayerNoDrugoi(GameSprite):      
    def walk(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 400:
            self.rect.y += self.speed

lost_one = 0
lost_two = 0

x1 = 0
y1 = 200

x2 = 675
y2 = 200

player_one = PlayerNoDrugoi('racketka.png', x1, y1, 5, 20, 100) 
player_two = Player('racketka.png', x2, y2, 5, 20, 100) 



















finish = False
game = True
while game:
    
    #window.blit(win,(, ))

    for e in event.get():
        if e.type == QUIT:
            game = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                pupa.fire()

    if finish != True:
        window.blit(background,(0, 0))
        player_one.reset()
        player_two.reset()
        player_one.walk()
        player_two.walk()

        #myach.draw(window)
        #myach.update()

        
        #chtoto = font1.render('Пропущенно:' + str(lost), True, (230, 230, 250))
        #window.blit(chtoto,(0, 10))
        #lalala = font1.render('Очки:' + str(score), True, (230, 230, 250))
        #window.blit(lalala,(0, 40))


    if lost_one >= 3:
        finish = True
        player_one.rect.x = 350
        player_one.rect.y = 400
        player_two.rect.x = 350
        player_two.rect.y = 400
        window.blit(lose_one, (100, 100))
    if lost_two >= 3:
        finish = True
        player_one.rect.x = 350
        player_one.rect.y = 400
        player_two.rect.x = 350
        player_two.rect.y = 400
        window.blit(lose_two, (100, 100))    

    


    clock.tick(FPS)
    display.update()
