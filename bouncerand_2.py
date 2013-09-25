import sys, pygame, random
from pygame.locals import *
pygame.init()

redspeed = [10, 10]
pingspeed = [5, 5]
pacspeed = [15, 15]
black = 0, 0, 0

red = pygame.image.load("red.png")
redrect = red.get_rect()

ping = pygame.image.load("ping.jpg")
pingrect = ping.get_rect()

pac = pygame.image.load ("pac.gif")
pacrect = pac.get_rect()

screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
WIDTH, HEIGHT = screen.get_size()
        
while 1:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                sys.exit()
                pygame.quit()
                
    redrect = redrect.move(redspeed)
    if redrect.left < 0 or redrect.right > WIDTH:
        redspeed[0] = -redspeed[0]                
    if redrect.top < 0 or redrect.bottom > HEIGHT:
        redspeed[1] = -redspeed[1]

    pingrect = pingrect.move(pingspeed)
    if pingrect.left < 0 or pingrect.right > WIDTH:
        pingspeed[0] = -pingspeed[0]                
    if pingrect.top < 0 or pingrect.bottom > HEIGHT:
        pingspeed[1] = -pingspeed[1]

    pacrect = pacrect.move(pacspeed)
    if pacrect.left < 0 or pacrect.right > WIDTH:
        pacspeed[0] = -pacspeed[0]                
    if pacrect.top < 0 or pacrect.bottom > HEIGHT:
        pacspeed[1] = -pacspeed[1]
    
    screen.fill(black)
    screen.blit(red, redrect)
    screen.blit(ping, pingrect)
    screen.blit(pac, pacrect)
    pygame.display.flip()
    