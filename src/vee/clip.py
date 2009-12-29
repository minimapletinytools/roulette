class Clip():
	"""
	Vclip is an abstract class 
	"""
	def __init__(self,xml):
		self.xml = xml
		self.playing = False
		#todo add some type of transition priority map container in here
	def play(self):
		pass 
	def preload(self):
		pass
	def grabFrame(self):
		pass
	def grabFrameNumber(self):
		#returns -1 for last frame
		pass
	def grabFrameTime(self):
		pass
class DummyClip(Clip):
	"""
	dummy clip, does nothing, used as blank trnansitional nodes in graph
	"""
	def __init__(self,xml):
		Clip.__init__(self,xml)
	def grabeFrameNumber(self):
		return -1
	def grabFrameTime(self):
		return -1
	
from pyglet import resource
import pyglet
import time
import utils
class ImageClip(Clip):
	def __init__(self,xml):
		Clip.__init__(self,xml)
		
		#do we presume by default that we want to load sound automatically or do we wnat to make another preload function for loading sound???
		self.sound = resource.media(xml.getAttribute("sound"),True)    #do we want to stream or not??? 
		self.start = 0
	def play(self):
		self.start = time.time()
		self.sound.play() #make sure there is no delay between this and when the sound plays
	def getTime(self):
		if self.start:
			return time.time()-self.start
		else: return 0
	def preload(self):
		#consider some sort of locals storage of image data in frame number to image map
		#either use good ole image wheel or allow for local creation of some sort of image wheel to maintain modularity
		#or to be lazy don't do anything
		pass
	def grabFrame(self):
		#TODO you should really make at least a local dict of image names to map becaus ethis loads the same image multiple times...
		#print self.xml,"frame","number",self.grabFrameNumber()
		framexml = utils.getChildWithAttribute(self.xml,"frame","number",self.grabFrameNumber())
		if framexml:
			return resource.image(framexml.getAttribute("filename"))
		else: return None
	def grabFrameNumber(self):
		return str((int)(self.getTime()/((int)(self.xml.getAttribute("durinms"))/1000.0)))
	def grabFrameTime(self):
		pass
		#TODO return sound playtime...

class VideoClip(Clip):
	"""
	plays a video clip, not implementede yet
	"""
	def __init__(self,xml):
		Clip.__init__(self,xml)
		
