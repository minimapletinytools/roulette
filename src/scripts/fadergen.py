import pygame
import math
from pygame import gfxdraw

folder = "/home/user/Desktop/Link to stalls/kitchen/faucet01/roulette/src/data/fader/fadein/"
prefix = "fadein"

size = w,h = 640,480
diag = 50
center = size[0]/2,size[1]/2
iterations = 20
color = 0,0,0
bgcolor = 255,255,255

rmin =  -200
rmax = 200
rstart = -100
rend = 600

pygame.init()
screen = pygame.display.set_mode(size,pygame.DOUBLEBUF)
screen.fill((255,255,255))

class diamond():
    def __init__(self,x,y):
        self.x,self.y = x,y
        self.odiag = diag
        self.diag = diag
    def draw(self,screen):
        #apply transformation to x,y if needed
        tx,ty = self.x,self.y
        #calculate pts
        pts = [(tx,ty+self.diag/2),(tx+self.diag/2,ty),(tx,ty-self.diag/2),(tx-self.diag/2,ty)]
        gfxdraw.filled_polygon(screen,pts,color)
        
#create big list of diamonds
diam = list()
for i in range(0,int(w*1.3/diag)):
    for j in range(0,int(h*2.3/diag)):
        diam.append(diamond(i*diag-(j%2)*diag/2,j*diag/2-diag/2))
def p():
    return (iterations-i)/float(iterations)
def q():
    return 1-p()
def d(x,y):
    return math.sqrt((x-center[0])*(x-center[0]) + (y-center[1])*(y-center[1]))
for i in range(0,iterations):
    radius = rstart*p()  + rend*q()
    print radius
    screen.fill(bgcolor)
    for e in diam:
        v = (d(e.x,e.y) - radius)
        if v < rmin:
            e.diag = 0
	elif v > rmax:
	    e.diag = diag
	else:
	    e.diag = diag*math.sqrt(math.fabs((v-rmin)/float(rmax - rmin)  -.1 ))
    for e in diam:
        e.draw(screen)
    pygame.image.save(screen,folder+prefix+str(i).zfill(5)+".png")
    pygame.display.flip()
