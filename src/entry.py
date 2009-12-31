from vee import win
from vee import controller
from vee import drawer
from xml.dom import minidom
from pyglet import resource
import pyglet

class roulette(win.Win):
    def __init__(self,*args, **kwargs):
        win.Win.__init__(self,*args, **kwargs)
        self.cont = controller.Controller(minidom.parse(resource.file("graph.xml")).documentElement)
        #setup the drawer module with current window vars. Since we have to do this, it might be better if we make drawer a singleton
        drawer.setVars(self)
    def update(self,dt):
        self.cont.update()
    def on_draw(self):
        self.cont.draw()
    def press(self):
        pass
    
    
def run():
    #w = roulette(fullscreen = True)
    w = roulette()
    pyglet.app.run()
if __name__ == "__main__":
    run()