import pygame
import time
WIDTH=400
HEIGHT=600
pygame.init()

#game vars
gravity=3
gravity_bar=10
i=0

#screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Sprimo')
clock = pygame.time.Clock()
fps = 60

#charji les images
character=pygame.image.load('assets/character.png').convert_alpha()
backgroung=pygame.image.load('assets/bg.png').convert_alpha()

#character class 
class Character():
    def __init__(self,x,y):
     self.image=pygame.transform.scale(character,(60,60))
     self.rect=self.image.get_rect()
     self.rect.center=(x,y)
     self.flip=False
     self.y=y
    def draw (self):
        screen.blit(pygame.transform.flip(self.image,self.flip,False),self.rect)
        pygame.draw.rect(screen,(255,0,0),self.rect,2)
    def move(self):
        keys=pygame.key.get_pressed()
        if keys[pygame.K_q] and self.rect.x>0:
            self.rect.x-=5
            self.flip=True
        if keys[pygame.K_d] and self.rect.x<WIDTH-60:
            self.rect.x+=5
            self.flip=False
        #gravity logic
        self.y+=gravity
        self.rect.y=self.y
        if self.rect.bottom> HEIGHT:
            for i in range(10):
                self.y -= gravity_bar
                
   
       
#Les object  
character=Character(WIDTH/2,HEIGHT-200)

#loop dyal lgame bach tb9a khdama 
run = True
while run:
    clock.tick(fps)
    screen.blit(backgroung,(-100,-150))
    character.draw()
    character.move()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()


#end game
pygame.quit()