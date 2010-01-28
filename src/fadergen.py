import pygame
from pygame import gfxdraw

size = w,h = 640,480
diag = 60
center = size[0]/2,size[1]/2
iterations = 20
color = 0,0,0
bgcolor = 255,255,255

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

for i in range(0,iterations):
    print i
    screen.fill(bgcolor)
    for e in diam:
        e.diag *= .93
    for e in diam:
        e.draw(screen)
    pygame.display.flip()