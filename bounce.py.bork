import sys, pygame
from pygame.locals import *
pygame.init()

#size = width, height = 1950, 1050

speed = [10, 10]
black = 0, 0, 0
red = 255, 0, 0

#screen = pygame.display.set_mode(size)

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
                pygame.quit()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        
    redrect = redrect.move(speed)
    if redrect.left < 0 or redrect.right > WIDTH:
        speed[0] = -speed[0]
    if redrect.top < 0 or redrect.bottom > HEIGHT:
        speed[1] = -speed[1]
                
                
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    pingrect = pingrect.move(speed)
    if pingrect.left < 0 or pingrect.right > WIDTH:
        speed[0] = -speed[0]
    if pingrect.top < 0 or pingrect.bottom > HEIGHT:
        speed[1] = -speed[1]
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    pacrect = pacrect.move(speed)
    if pacrect.left < 0 or pacrect.right > WIDTH:
        speed[0] = -speed[0]
    if pacrect.top < 0 or pacrect.bottom > HEIGHT:
        speed[1] = -speed[1]
        
    screen.fill(black)
    screen.blit(red, redrect)
    screen.blit(ping, pingrect)
    screen.blit(pac, pacrect)
    pygame.display.flip()
    