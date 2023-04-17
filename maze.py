from pygame import *
mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()
money=mixer.Sound('money.ogg')
kick=mixer.Sound('kick.ogg')
font.init()
font=font.SysFont('Arial',70)
window=display.set_mode((700,500))
class GameSprite(sprite.Sprite):
    def __init__(self,img,x,y,speed):
        super().__init__()
        self.img=transform.scale(image.load(img),(75,75))
        self.speed=speed
        self.rect=self.img.get_rect()
        self.rect.x=x
        self.rect.y=y
    def reset(self):
        window.blit(self.img,(self.rect.x,self.rect.y))
class Player(GameSprite):
    def __init__(self,img,x,y,speed):
        super().__init__(img,x,y,speed)
    def update(self):
        keys_pressed=key.get_pressed()
        if keys_pressed[K_w] and self.rect.y>=0:
            self.rect.y-=self.speed
        if keys_pressed[K_s] and self.rect.y<=400:
            self.rect.y+=self.speed
        if keys_pressed[K_a] and self.rect.x>=0:
            self.rect.x-=self.speed
        if keys_pressed[K_d] and self.rect.x<=600:
            self.rect.x+=self.speed

class Enemy(GameSprite):
    def __init__(self,img,x,y,speed,direction):
        super().__init__(img,x,y,speed)
        self.direction=direction
    def update(self):
        x1=450
        x2=600
        
        if self.direction=='left':
            if self.rect.x<=x1:
                self.direction='right'
            else:
                self.rect.x-=self.speed
        if self.direction=='right':
            if self.rect.x>=x2:
                self.direction='left'
            else:
                self.rect.x+=self.speed
class Wall(sprite.Sprite):
    def __init__(self,col1,col2,col3,width,height,x,y):
        super().__init__()
        self.col1=col1
        self.col2=col2
        self.col3=col3
        self.width=width
        self.height=height
        self.image=Surface((self.width,self.height))
        self.image.fill((col1,col2,col3))
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
    def draw_wall(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
display.set_caption('Лабиринт')
background=transform.scale(image.load('background.jpg'),(700,500))
sprite2=Enemy('cyborg.png',550,200,2,'left')
sprite1=Player('hero.png',0,0,6)
sprite3=GameSprite('treasure.png',550,400,0)
wall1=Wall(199,199,0,5,350,250,15)
wall2=Wall(199,199,0,5,400,100,100)
wall3=Wall(199,199,0,5,400,400,100)
wall4=Wall(199,199,0,50,5,350,400)
game=True
finish=False
clock=time.Clock()
fps=60
lose=font.render('YOU LOSE!',True,(255,0,0))
win=font.render('YOU WIN!',True,(255,215,0))
while game:
    for e in event.get():
        if e.type == QUIT:
            game=False
    if finish!=True:
        clock.tick(fps)
        window.blit(background,(0,0))
        sprite1.reset()
        sprite1.update()
        sprite2.reset()
        sprite2.update()
        sprite3.reset()
        wall1.draw_wall()
        wall2.draw_wall()
        wall3.draw_wall()
        wall4.draw_wall()
        if sprite.collide_rect(sprite1,sprite2) or sprite.collide_rect(sprite1,wall1) or sprite.collide_rect(sprite1,wall2) or sprite.collide_rect(sprite1,wall3) or sprite.collide_rect(sprite1,wall4):
            finish=True
            kick.play()
            window.blit(lose,(200,200))
        if sprite.collide_rect(sprite1,sprite3):
            finish=True
            money.play()
            window.blit(win,(200,200))
    display.update()
