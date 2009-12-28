#~ class lol:
    #~ def f(self):
        #~ print "called f"
#~ class rofl(lol):
    #~ def __init__(self):
        #~ print "we do not initialize anything"

#~ import pyglet
#~ from pyglet.gl import *
#~ window = pyglet.window.Window()

#~ @window.event
#~ def on_draw():
    #~ glClear(GL_COLOR_BUFFER_BIT)
    #~ img = pyglet.image.load("data/gray8a_bk.png")
    #~ glEnable (GL_BLEND)
    #~ glBlendFunc (GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    #~ img.blit(0,0)

#~ glClearColor(1.0,0,0,1)
#~ pyglet.app.run()
