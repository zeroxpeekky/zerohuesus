from pygame import *
font.init()


window = display.set_mode((700,500))
display.set_caption('maze')
zadniyfon = transform.scale(image.load("background.jpg"),(700,500))

clock = time.Clock()

x1 = 50
y1 = 10
x2 = 100
y2 = 100

mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()
font = font.Font

class Wall(sprite.Sprite):
    def __init__(self, color_1,wall_x,wall_y,wall_width,wall_height):
        super().__init__()
        self.color_1 = color_1
        self.width = wall_width
        self.height = wall_height
        self.image = Surface((self.width,self.height))
        self.image.fill(color_1)
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        window.blit(self.image,(self.rect.x, self.rect.y))
    

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Monster(GameSprite):
    direction = "left"
    def update(self):
        if self.rect.x <= 470:
            self.direction = "right"
        if self.rect.x >= 620:
            self.direction = "left"
        if self.direction == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed
        
class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys [K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys [K_RIGHT] and self.rect.x < 600:
            self.rect.x += self.speed
        if keys [K_DOWN] and self.rect.y < 450:
            self.rect.y += self.speed
        if keys [K_UP] and self.rect.y > 10:
            self.rect.y -= self.speed
player = Player('hero.png', 5 , 400, 4)
monster = Monster('cyborg.png',  600, 400, 2)
final = GameSprite('treasure.png',600, 400, 0)
w1 = Wall((154, 205, 50), 100, 20 , 450, 10)
w2 = Wall((154, 205, 50), 100, 480, 350, 10)
w3 = Wall((154, 205, 50), 100, 20 , 10, 380) 
w4 = Wall((154, 205, 50), 200, 130, 10, 350)
w5 = Wall((154, 205, 50), 450, 130, 10, 360)
w6 = Wall((154, 205, 50), 300, 20, 10, 350)
w7 = Wall((154, 205, 50), 390, 120, 130, 10) 
Wall = [w1,w2,w3,w4,w5,w6,w7]

finish = False
game = True
while game == True:
    window.blit(zadniyfon,(0,0))
    
    
   
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.blit(zadniyfon,(0,0))
        player.update()
        for w in Wall:
            w.draw_wall()
        monster.update()
        player.reset()
        monster.reset()
        final.reset()
    sprite.collide_rect(player, final)
    sprite.collide_rect(player, monster)
    sprite.collide_rect(player, w)
    if sprite.collide_rect(player, monster) or sprite.collide_rect(player,w):
        finish = True
        window.blit(lose(200,200))
        kick.play()
    display.update()
    clock.tick(60)
