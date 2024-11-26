import pygame
WIDTH=400
HEIGHT=600
pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Sprimo')

#charji les images
character=pygame.image.load('assets/character.png').convert_alpha()
backgroung=pygame.image.load('assets/bg.png').convert_alpha()

#character class 
class Character():
    def __init__(self,x,y):
     self.image=pygame.transform.scale(character,(60,60))
     self.rect=self.image.get_rect()
     self.rect.center=(x,y)
    def draw (self):
        screen.blit(self.image,self.rect)
        pygame.draw.rect(screen,(255,0,0),self.rect,2)

#Les object  
character=Character(WIDTH/2,HEIGHT-100)

#loop dyal lgame bach tb9a khdama 
run = True
while run:
    screen.blit(backgroung,(-100,-150))
    character.draw()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()


#end game
pygame.quit()