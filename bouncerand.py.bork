import sys, pygame, random
from pygame.locals import *
pygame.init()

#size = width, height = 1950, 1050

speed = [10, 10]
speed1 = [10, 10]
speed2 = [10, 10]
speed3 = [10, 10]
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
                sys.exit()
                pygame.quit()
        
    redspeed = speed1
    redrect = redrect.move(speed1)
    if redrect.left < 0 or redrect.right > WIDTH:
            redspeed[1] = -speed1[1]
            if redspeed [1] < 0:
                redspeed[1] = random.randint(1,20)
                redspeed[1] = -speed1[1]
            else:
                speed1[0] = -random.randint(1,20)
                
    if redrect.top < 0 or redrect.bottom > HEIGHT:
        redspeed[1] = -speed1[1]
        if redspeed[1] < 0:
            redspeed[1] = random.randint(1,20)
            redspeed[1] = -speed1[1]
            
    pingspeed = speed2
    pingrect = pingrect.move(pingspeed)
    if pingrect.left < 0 or pingrect.right > WIDTH:
            pingspeed[0] = -pingspeed[0]
            if pingspeed [1] < 0:
                pingspeed[1] = random.randint(1,20)
                pingspeed[1] = -pingspeed[0]
            else:
                pingspeed[0] = -random.randint(1,20)
                
    if pingrect.top < 0 or pingrect.bottom > HEIGHT:
        pingspeed[1] = -pingspeed[1]
        if pingspeed[1] < 0:
            pingspeed[1] = random.randint(1,20)
            pingspeed[1] = -pingspeed[1]
            
    pacspeed = speed3
    pacrect = pacrect.move(pacspeed)
    if pacrect.left < 0 or pacrect.right > WIDTH:
            pacspeed[0] = -pacspeed[0]
            if pacspeed [1] < 0:
                pacspeed[1] = random.randint(1,20)
                pacspeed[1] = -pacspeed[0]
            else:
                pacspeed[0] = -random.randint(1,20)
                
    if pacrect.top < 0 or pacrect.bottom > HEIGHT:
        speed[1] = -speed[1]
        if speed[0] < 0:
            speed[1] = random.randint(1,20)
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
    