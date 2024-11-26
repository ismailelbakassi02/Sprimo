import pygame
WIDTH=400
HEIGHT=600
pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Sprimo')

#charji les images
player=pygame.image.load('assets/player.png').convert_alpha()
backgroung=pygame.image.load('assets/bg.png').convert_alpha()

#player class 
class Player():
    def __init__(self,x,y):
     self.image=player
#loop dyal lgame bach tb9a khdama 
run = True
while run:
    screen.blit(backgroung,(-100,-150))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()


#end game
pygame.quit()