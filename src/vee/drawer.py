#TODO this whole drawing nonsense is pretty awful, but until you can figure out something better, stick with this
#determine variables

from pyglet.gl import *
#glClearColor(0,0,0,0)
#glEnable(GL_BLEND)
#glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

width,height = None,None
init = False

def setVars(window):
    """
    sets variables for drawing
    window should be of class pyglet.window.Window
    """
    global width,height,init
    width = window.width
    height = window.height
    init = True
    window.clear()
    print "you are runnig at resoultion",width,height

def largestrect(r1w,r1h,r2w,r2h):
    """returns w,h such that r1 fits in r2 without change in ratio"""
    if(r1w/r1h < r2w/r2h):
        return r2w, r2w*r1h/r1w
    else:
        return r2h*r1w/r1h, r2h
    
def draw(img,ox = 0, oy = 0):
    global width,height,init
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    if init and img:
        w,h = largestrect(img.width,img.height,width-ox,height-oy)
        #drawing from lower left corner
        img.blit((width-w)/2,(height-h)/2,0,w,h)
