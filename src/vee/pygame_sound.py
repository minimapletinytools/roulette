#consider building singleton interface wrapper
#also consider providing access to pyglet sound library as well
import pygame
from pyglet.resource import *
class Sound:
    def __init__(self):
        pygame.mixer.pre_init(44100, -16, 2, 2048)
        pygame.init()
        self.soundList = dict()
        self.activemusic = None
    #for more robust version, build error checking into music part of this class
    def loadMusic(self,filename):
        if self.activemusic != filename:
            self.activemusic = filename
            pygame.mixer.music.load(file(filename))
    def playMusic(self,filename):
        if self.activemusic != filename:
            self.loadMusic(filename)
        self.mixer.music.play()
    def stopMusic(self):
        self.mixer.music.stop()
    def getSound(self,filename):
        if filename not in self.soundList:
            self.loadSound(filename)
        return self.soundList[filename]
    def loadSound(self,filename):
        """loads sound filename and puts it on the flywheel
        
        filename: string"""
        if filename not in self.soundList:
            self.soundList[filename] = pygame.mixer.Sound(file(filename))
            print "loaded sound", filename, self.soundList[filename]
        
    def play(self, filename):
        if filename not in self.soundList:
            self.loadSound(filename)
        #print "playing sound",filename
        self.soundList[filename].play()
    
    def stopAll(self):
        pygame.mixer.stop()
