#consider building singleton interface wrapper
#also consider providing access to pyglet sound library as well
import pygame
from pyglet.resource import *
class Sound:
    def __init__(self):
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
        if not filename:
            return None
        if filename not in self.soundList:
            self.loadSound(filename)
        return self.soundList[filename]
    def isPlaying(self,filename):
        return self.getSound(filename).get_num_channels()
    def loadSound(self,filename):
        """loads sound filename and puts it on the flywheel
        
        filename: string"""
        if not filename:
            return filename
        if filename not in self.soundList:
            self.soundList[filename] = pygame.mixer.Sound(file(filename))
            print "loaded sound", filename, self.soundList[filename]
        return filename
    def play(self, filename):
        if not filename:
            return
        if filename not in self.soundList:
            self.loadSound(filename)
        print "playing sound",filename
        self.soundList[filename].play()
    def stop(self,filename):
        if filename in self.soundList:
            print "stopped",filename
            self.soundList[filename].stop()
    def stopAll(self):
        print "stopping all sound"
        pygame.mixer.stop()
