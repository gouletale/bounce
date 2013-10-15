from stuff import *
from southpark import *

class Kenny(Stuff):

    self.kennyImages = ["1.psd", "2.psd", "3.psd", "4.psd", "5.psd", "6.psd", "7.psd", "8.psd", "9.psd", "10.psd"]
    self.i = 0
    
    def __init__(self, image, a, b):
        self.speed = [a, b]
        self.image = image
        self.stuff = None
        self.stuffrect = None
        
        self.setup(self.kennyImages)
    
    def update(self):
        self.stuffrect = self.stuffrect.move(self.speed)
        if self.stuffrect.left < 0 or self.stuffrect.right > width:
            self.speed[0] = -self.speed[0]
            #Select next image in list
            
            self.image = self.kennyImages[i]
            self.i += 1
            self.setup()

        if self.stuffrect.top < 0 or self.stuffrect.bottom > height:
            self.speed[1] = -self.speed[1]
            #Select next image in list
            self.setup()