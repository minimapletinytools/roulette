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
	def stop(self):
		pass
	def preload(self,video = True,sound = True):
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
import glob
import stupid
class ImageClip(Clip):
	def __init__(self,xml):
		Clip.__init__(self,xml)
		
		#do we presume by default that we want to load sound automatically or do we wnat to make another preload function for loading sound???()
		#TODO make blank sound thingy
		self.sound = glob.sound.loadSound(xml.getAttribute("sound"))
		self.start = 0
	def play(self):
		self.start = time.time()
		glob.sound.play(self.sound)
	def stop(self):
		glob.sound.stopAll()
	def getTime(self):
		if self.start:
			return time.time()-self.start
		else: return 0
	def preload(self,video = True,sound = True):
		#consider some sort of locals storage of image data in frame number to image map
		#either use good ole image wheel or allow for local creation of some sort of image wheel to maintain modularity
		#or to be lazy don't do anything
		pass
	def grabFrame(self):
		n = self.grabFrameNumber()
		if int(n) <= int(self.xml.getAttribute("frames")):
			#print stupid.splitjoin(self.xml.getAttribute("folder")+self.xml.getAttribute("prefix")+n.zfill(5)+".jpg")
			return resource.image(stupid.splitjoin(self.xml.getAttribute("folder")+self.xml.getAttribute("prefix")+n.zfill(5)+".jpg"))
		return None
	def grabFrameOLD(self):
		#TODO you should really make at least a local dict of image names to map becaus ethis loads the same image multiple times...
		#print self.xml,"frame","number",self.grabFrameNumber()
		framexml = utils.getChildWithAttribute(self.xml,"frame","number",self.grabFrameNumber())
		if framexml:
			return resource.image(stupid.splitjoin(framexml.getAttribute("folder")+framexml.getAttribute("filename")))
		else: return None
	def isFinished(self):
		if self.start:
			if self.xml.hasAttribute("duration"):
				return self.getTime() > float(self.xml.getAttribute("duration"))
			else: return self.getTime() > self.sound.duration 
		return False
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
		
