"""
global.py contains constants and any other global variables if needed
"""

motd = "Roulette v.01\na game by Peter Lu\nRoulette is built on python v2.6"
import sys
print "You are running python version,",sys.version
print motd

import pyglet
#glClearColor(255,255,255,0)
    
pyglet.options['audio'] = ('alsa', 'alsa', 'directsound','silent')
pyglet.resource.path.append("data")
#TODO this is probably not a good idea, yous hould really allow for directories, use split and then rejoin with os.path.join
pyglet.resource.path.append("data/sound")
pyglet.resource.reindex()



import pygame
import pygame_sound
import imagewheel
pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.init()
joy = None
if pygame.joystick.get_count() > 0:
    joy = pygame.joystick.Joystick(0)
    joy.init()
sound = pygame_sound.Sound()
wheel = imagewheel.ImageWheel()