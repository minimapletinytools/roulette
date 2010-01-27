import time
from pyglet.text import document,layout
class Subtitles():
    #todo implements a document and textlayout object
    #document has static formatting and text layout 
    #font size calculated relative to screen size
    def __init__(self):
        self.activeSub = document.UnformattedDocument("default text but there is more here haha lololol what is going on")
        self.activeSub.set_style(0, len(self.activeSub.text), 
            dict(color=(255, 255, 255, 255),font_size=25,align="center")
        )
        self.layout = layout.TextLayout(self.activeSub,600,200,multiline=True)
        self.layout.x = 300
        self.layout.anchor_x = "center"
        self.layout.anchor_y = "center"
        self.layout.y = 25
        self.playing = False
        self.loaded = False
        self.updated = False
        self.startTime = 0
        self.stopTime = 0
    def loadSub(self,text,playtime,start = 0):
        self.activeSub.text = text
        self.startTime = start + time.time()
        self.stopTime = self.startTime + playtime
        self.loaded = True
    def update(self):
        t = time.time()
        if t > self.startTime and t < self.stopTime:
            self.playing = True
        if t > self.stopTime:
            self.playing = False
            self.loaded = False
        self.updated = True
    def draw(self):
        self.layout.draw()
        if not self.updated:
            self.update()
        if self.playing and time.time():
            #TODO render text
            pass
        self.updated = False