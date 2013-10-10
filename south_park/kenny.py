import Stuff_class

class Kenny(Stuff):

    def update(self):
        self.stuffrect = self.stuffrect.move(self.speed)
        if self.stuffrect.left < 0 or self.stuffrect.right > width:
            self.speed[0] = -self.speed[0]
            #Select next image in list
            self.setup()
            while i 
        if self.stuffrect.top < 0 or self.stuffrect.bottom > height:
            self.speed[1] = -self.speed[1]
            #Select next image in list
            self.setup()
            
kenny = Kenny("kenny.psd", a, b)