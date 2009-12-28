import Vglobal
import sys
import pyglet
from pyglet import window

class Vclip():
	def __init__(self,xml):
		self.xml = xml
		#load audio
	def getImage():
		pass
		#checks audio time and returns an image in sync to audio time
		#decide what to do when a`udio playback is over (return same image or return images in sequence based on timer)
		
class Vwin( window.Window ): 
	def __init__(self):
		window.Window()
		keys = window.key.KeyStateHandler()
		self.push_handlers(keys)
		pass
	def on_key_press(self,symbol,modifiers):
		print "on key press:",symbol,modifiers
		if symbol == window.key.SPACE:
			print "space pressd"
			self.press()
	def press(self):
		pass
		
if __name__ == "__main__":
	print "now running test application"
	win = Vwin()
	pyglet.app.run()