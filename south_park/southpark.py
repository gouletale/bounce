import sys, pygame, random
from kenny import *
from stuff import *
from pygame.locals import *
pygame.init()

images = ["stan.psd", "kyle.psd", "cartman.psd"]
kenny_image = "kenny.psd"

list_of_stuff = []
a = random.randint(1, 15)
b = random.randint(1, 15)

black = 0, 0, 0

screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
width, height = screen.get_size()
        
for image in images:
    stuff = Stuff(image, random.randint(1,15), random.randint(1,15))
    list_of_stuff.append(stuff)
kenny_image_as_class = kenny_class(kenny_image, random.randint(1,15), random.randint(1,15))
    


        
while 1:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                sys.exit()
                pygame.quit()
                

    screen.fill(black)
    for stuff in list_of_stuff:
        stuff.update()
        stuff.render(screen)
    
    kenny_image_as_class.update()
    kenny_image_as_class.render(screen)
    pygame.display.flip()
    