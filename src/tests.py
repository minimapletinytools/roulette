#===============================================================================
# #globals locals test
# x = 1
# def l():
#    print "you are in l"
# def f():
#    l()
#    print "locals", locals()
#    global x
#    x = 2
#    print "locals", locals()
#    #print "globals", globals()
#===============================================================================

#~ class lol:
    #~ def f(self):
        #~ print "called f"
#~ class rofl(lol):
    #~ def __init__(self):
        #~ print "we do not initialize anything"

import pyglet
from pyglet.gl import *
window = pyglet.window.Window()

@window.event
def on_draw():
    glClear(GL_COLOR_BUFFER_BIT)
    for i in range(100):
        img = pyglet.image.load("words/gauresized.jpg")
    glEnable (GL_BLEND)
    glBlendFunc (GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    img.blit(0,0,0,2000,400)
    print "lolspourT"
@window.event
def update():
    print "updating"

glClearColor(1.0,0,0,1)
pyglet.app.run()
