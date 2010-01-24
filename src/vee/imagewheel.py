from pyglet import resource
class ImageWheel:
    def __init__(self):
        self.iMap = dict()
    def loadImage(self,filename):
        if filename not in self.iMap:
            self.iMap[filename] = resource.image(filename)
    def getImage(self,filename):
        if filename not in self.iMap:
            self.loadImage(filename)
        return self.iMap[filename]
        