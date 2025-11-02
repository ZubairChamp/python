import pygame
pygame.init()
screen=pygame.display.set_mode((10000,10000))
done=False
while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
    pygame.draw.circle(screen,(255,0,0),(300,300),50)
    pygame.display.flip()