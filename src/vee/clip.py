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
	def getTimeLeft(self):
		pass
	def skip(self):
		#jumps to end of frame
		pass
	
class DummyClip(Clip):
	"""
	dummy clip, does nothing, used as blank transitional nodes in graph
	"""
	def __init__(self,xml):
		Clip.__init__(self,xml)
	def grabeFrameNumber(self):
		return -1
	def grabFrameTime(self):
		return -1
	def isFinished(self):
		return True
	
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
		self.sound = xml.getAttribute("sound")
		self.start = 0
		self.freeze = False
		if xml.hasAttribute("freeze") and xml.getAttribute("freeze") == "yes":
			self.freeze = True
	def play(self):
		self.start = time.time()
		glob.sound.play(self.sound)
	def stop(self):
		pass
		#glob.sound.stopAll()
	def getTime(self):
		if self.start:
			return time.time()-self.start
		else: return 0
	def getTimeLeft(self):
		return self.getLength() - self.getTime()
	def getLength(self):	
		if self.xml.hasAttribute("duration"):
			return float(self.xml.getAttribute("duration"))
		elif self.sound: 
			return glob.sound.getSound(self.sound).get_length()
		else:
			print "time left error" 
			return 0
	def preload(self,video = True,sound = True):
		if sound:
			glob.sound.loadSound(self.sound)
		if video:
			pass #TODO load all images
	def grabFrame(self):
		"""
		this version of grab frame asumes the timing information is in the clip xml node and extrapolates image number based on time
		"""
		#this version does not allow for "freezing" on last frame and requires looping otherwise returns None -> nothing is drawn
		#todo implement freezing, this should be a either a CLIP property or a GRAPHNODE property that overrides whatever the CLIP property is
		n = self.grabFrameNumber()
		if int(n) <= int(self.xml.getAttribute("frames"))-1:
			#print stupid.splitjoin(self.xml.getAttribute("folder")+self.xml.getAttribute("prefix")+n.zfill(5)+".jpg")
			return resource.image(stupid.splitjoin(self.xml.getAttribute("folder")+self.xml.getAttribute("prefix")+n.zfill(5)+".png"))
		#return the last frame in the clip if we specify freeze = True
		if self.freeze:
			n = str(int(self.xml.getAttribute("frames"))-1)
			return resource.image(stupid.splitjoin(self.xml.getAttribute("folder")+self.xml.getAttribute("prefix")+n.zfill(5)+".png"))
		return None
	def grabFrameOLD(self):
		"""
		this version of grabframe assumes that the clip xml node has all its images listed with their respective times.
		Use this version if you want to have a non constant speed animation.
		"""
		#TODO you should really make at least a local dict of image names to map becaus ethis loads the same image multiple times...
		#print self.xml,"frame","number",self.grabFrameNumber()
		framexml = utils.getChildWithAttribute(self.xml,"frame","number",self.grabFrameNumber())
		if framexml:
			return resource.image(stupid.splitjoin(framexml.getAttribute("folder")+framexml.getAttribute("filename")))
		else: return None
	
	def isFinished(self):
		"""
		returns true if clip has started playing and is finished playing
		if duration is specified in xml, this returns if playtime exceeds duration
		otherwise duration in sound is used
		"""
		#TODO add some type of error handling in case sound object does not exist
		if self.start:
			if self.getTimeLeft() <= 0:
				return True
			else: return False
			#if self.xml.hasAttribute("duration"):
			#	return self.getTime() > float(self.xml.getAttribute("duration"))
			#else: return self.getTime() > glob.sound.getSound(self.sound).get_length() 
		return False
	def grabFrameNumber(self):
		return str((int)(self.getTime()/((int)(self.xml.getAttribute("durinms"))/1000.0)))
	def grabFrameTime(self):
		pass
		#TODO return sound playtime...
	def skip(self):
		self.start -= self.getLength()

import imagewheel
class CachedImageClip(ImageClip):
	"""
	identical to ImageClip except uses cached images
	"""
	def __init__(self,xml):
		ImageClip.__init__(self,xml)
	def grabFrame(self):
		#this version does not allow for "freezing" on last frame and requires looping otherwise returns None -> nothing is drawn
		#todo implement freezing, this should be a either a CLIP property or a GRAPHNODE property that overrides whatever the CLIP property is
		if self.xml.hasAttribute("suffix"): suffix = self.xml.getAttribute("suffix")
		else: suffix = ".png"
		n = self.grabFrameNumber()
		if int(n) <= int(self.xml.getAttribute("frames"))-1:
			#print stupid.splitjoin(self.xml.getAttribute("folder")+self.xml.getAttribute("prefix")+n.zfill(5)+".jpg")
			return glob.wheel.getImage(stupid.splitjoin(self.xml.getAttribute("folder")+self.xml.getAttribute("prefix")+n.zfill(5)+suffix))
		#return the last frame in the clip if we specify freeze = True
		if self.freeze:
			n = str(int(self.xml.getAttribute("frames"))-1)
			return glob.wheel.getImage(stupid.splitjoin(self.xml.getAttribute("folder")+self.xml.getAttribute("prefix")+n.zfill(5)+suffix))
		return None
	
class VideoClip(Clip):
	"""
	plays a video clip, not implementede yet
	"""
	def __init__(self,xml):
		Clip.__init__(self,xml)
		
