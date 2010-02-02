from pyglet import resource
from pyglet import image
import stupid
class ImageWheel:
    def __init__(self):
        self.iMap = dict()
    def loadImage(self,filename):
        if filename not in self.iMap:
            #self.iMap[filename] = resource.image(filename)
            try: self.iMap[filename] = image.load(stupid.splitjoin(filename))
            except: print "FAIL"
    def getImage(self,filename):
        if filename not in self.iMap:
            self.loadImage(filename)
        return self.iMap[filename]
        