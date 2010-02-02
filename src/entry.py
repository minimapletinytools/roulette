from vee import win
from vee import controller
from vee import drawer
from vee import subtitles
from xml.dom import minidom
from pyglet import resource
import pyglet
import time
import pygame

class roulette(win.Win):
    def __init__(self,*args, **kwargs):
        #win.Win.__init__(self,width=320,height=240,*args, **kwargs)
        win.Win.__init__(self,*args, **kwargs)
        self.cont = controller.Controller(minidom.parse(resource.file("jake_graph_FINAL.xml")).documentElement)
        self.sub = subtitles.Subtitles()
        #setup the drawer module with current window vars. Since we have to do this, it might be better if we make drawer a singleton
        drawer.setVars(self)
    def update(self,dt):
        #additional josytick handilng stuff here"
        for e in pygame.event.get():
            if e.type == pygame.JOYBUTTONDOWN and e.button == 1:
                self.press()
                self.pressTime = time.time()
            elif e.type == pygame.JOYBUTTONUP and e.button == 1:
                print e.button
                self.release(time.time()-self.pressTime)
        self.cont.update()
    def on_draw(self):
        self.cont.draw() 
        #self.sub.draw()
    def press(self):
        self.cont.press()
    def skip(self):
        self.cont.skip()
    def release(self,dt):
        self.cont.release(dt)
#===============================================================================
# import sys, os
# print "dirname", os.path.dirname(sys.executable)
# print "mainm odule", sys.modules['__main__']
# print "dirname of main module", os.path.dirname(sys.modules['__main__'].__file__)
#===============================================================================
def run():
    w = roulette(fullscreen = True)
    #w = roulette()
    w.set_exclusive_mouse()
    pyglet.app.run()
if __name__ == "__main__":
    run()
