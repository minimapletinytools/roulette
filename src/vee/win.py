import glob
import sys
import pyglet
from pyglet import window
		
class Win( window.Window ): 
	def __init__(self,*args, **kwargs):
		window.Window.__init__(self, *args, **kwargs)
		keys = window.key.KeyStateHandler()
		self.push_handlers(keys)
		pyglet.clock.schedule(self.update)
		#instantiate a controller
	def update(self,dt):
		"""
		update function
		"""
		pass
	def on_draw(self):
		pass
	def on_key_press(self,symbol,modifiers):
		print "key pressed:",symbol,modifiers
		if symbol == window.key.ESCAPE:
		    exit()
		if symbol == window.key.SPACE:
			print "space pressd"
			self.press()
	def press(self):
		pass
		
if __name__ == "__main__":
    run()

def run():
	print "now running test application"
	window = Win()
	pyglet.app.run()
