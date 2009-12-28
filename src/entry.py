from vee import win
from pyglet import resource
import pyglet

class roulette(win.Win):
    def __init__(self,*args, **kwargs):
        win.Win.__init__(self,*args, **kwargs)
    def update(self,dt):
		"""
		update function
		"""
		pass
    def on_draw(self):
        pass
    def press(self):
        pass
    
    
def run():
    w = roulette()
    #setup win.win here
    #test file loading okay
    f = resource.file("pal.png")
    print f
    pyglet.app.run()
if __name__ == "__main__":
    run()