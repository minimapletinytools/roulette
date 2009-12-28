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
class DummyClip(Vclip):
	"""
	dummy clip, does nothing, used as blank trnansitional nodes in graph
	"""
	def __init__(self,xml):
		Clip.__init__(self,xml)
	def grabeFrameNumber(self):
		return -1
	def grabFrameTime(self):
		return -1
class ImageClip(Vclip):
	def __init__(self,xml):
		Clip.__init__(self,xml)
		#TODO load image sequence information into frame number to image map
		#TODO load sound
	def play(self):
		self.playing = True
		#TODO start playing sound
	def  preload(self):
		#consider some sort of locals storage of image data in frame number to image map
		#either use good ole image wheel or allow for local creation of some sort of image wheel to maintain modularity
		#or to be lazy don't do anything
		pass
	def grabFrame(self):
		pass
		#use grabframenumber and return pyglet image
	def grabFrameNumber(self):
		pass
		#TODO read sound time and match to frame number
		#return last frame if sound has stopped playing
	def grabFrameTime(self):
		pass
		#TODO return sound playtime...

class VideoClip(Vclip):
	"""
	plays a video clip, not implementede yet
	"""
	def __init__(self,xml):
		Clip.__init__(self,xml)
		
