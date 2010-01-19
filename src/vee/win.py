import glob
import sys
import pyglet
import time
from pyglet import window
		
class Win( window.Window ): 
	def __init__(self,*args, **kwargs):
		window.Window.__init__(self, *args, **kwargs)
		#keys = window.key.KeyStateHandler()
		#self.push_handlers(keys)
		self.pressTime = 0
		pyglet.clock.schedule(self.update)
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
			self.pressTime = time.time()
			self.press()
	def on_key_release(self,symbol,modifiers):
		if symbol == window.key.SPACE:
			self.release(time.time()-self.pressTime)
	def press(self):
		pass
	def release(self,dt):
		pass
		
if __name__ == "__main__":
    run()

def run():
	print "now running test application"
	window = Win()
	pyglet.app.run()
