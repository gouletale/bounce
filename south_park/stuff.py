import sys, pygame, random
from pygame.locals import *
pygame.init()

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