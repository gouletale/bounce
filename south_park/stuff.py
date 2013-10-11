import sys, pygame, random
import kenny
import stuff
from pygame.locals import *
pygame.init()

images = ["stan.psd", "kyle.psd", "cartman.psd"]

list_of_stuff = []
a = random.randint(1, 15)
b = random.randint(1, 15)

black = 0, 0, 0

screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
width, height = screen.get_size()


class Stuff():

    def __init__(self, image, a, b):
        self.speed = [a, b]
        self.image = image
        self.stuff = None
        self.stuffrect = None
        
        self.setup()
        
    def setup(self):
        self.stuff = pygame.image.load(self.image)
        self.stuffrect = self.stuff.get_rect()
        
    def update(self):
        self.stuffrect = self.stuffrect.move(self.speed)
        if self.stuffrect.left < 0 or self.stuffrect.right > width:
            self.speed[0] = -self.speed[0]
        if self.stuffrect.top < 0 or self.stuffrect.bottom > height:
            self.speed[1] = -self.speed[1]
            
    def render(self, screen):
        screen.blit(self.stuff, self.stuffrect)
        
for image in images:
    stuff = Stuff(image, random.randint(1,15), random.randint(1,15))
    list_of_stuff.append(stuff)
    
kenny = ken("kenny.psd", random.randint(1,15), random.randint(1,15))

        
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

    pygame.display.flip()
    