import clip
import utils
import xml
from xml.dom import minidom
from pyglet import resource

class Controller:
	"""
	controller may as well be renamed as state, controller handles all state information, by default, it seems controller comes with a clip manager
	maybe it would be better if we could insert plugins into controller and plugins get controlled automatically by the state machine
	"""
	def __init__(self,xml):
		self.man = ClipManager(xml)
	def update(self):
		#todo update self.man, decide how to pass it state information
		pass
	def draw(self):
		self.man.draw()
		
import drawer
class ClipManager():
	class GraphNode:
		def __init__(self,xml):
			#TODO if xml is not element node, (i.e. it is document from just loaded xml file) then try and find an appropriate element node
			self.xml = xml
			#considering parsing xml data to native datatypes for slightly improved performance
		def getAttribute(self,prop):
			try: return self.xml.getAttribute(prop)
			except: return ""
		def getNext(state):
			"""
			returns id of next node if transition is to take place, returns -1 otherwise
			"""
			#TODO decide how you want ot handle state information
			pass
	def __init__(self,xml):
		self.active = "1"
		self.load(xml)
	def load(self,node):
		"""
		filename is location of graph xml data file.
		graph xml data file will contain information concerning clips
		"""
		self.graphxml = node
		self.clipxml = minidom.parse(resource.file(self.graphxml.getAttribute("clipxml")))
		#setup transition graph
		self.graphmap = dict()
		for e in utils.getChildren(self.graphxml,"clipnode"):
			self.graphmap[e.getAttribute("id")] = self.GraphNode(e)
		#set up clipmap
		self.clipmap = dict()
		for i in utils.getChildren(self.clipxml,"clip"):
			type = i.getAttribute("type")
			c = getattr(clip,type,clip.DummyClip)(i)
			self.clipmap[i.getAttribute("name")] = c
		self.getActiveClip().play()
	def draw(self):
		drawer.draw(self.getActiveClip().grabFrame())
		pass
	def getActiveClip(self):
		return self.clipmap[self.graphmap[self.active].getAttribute("clip")]
				
class Overlayer:
	def __init__(self):
		pass
	def update():
		pass
	def draw():
		pass
		
