import Vclip
from xml.dom import minidom

class Controller:
	def __init__(self,xml = None):
		activeClip = None
	def update():
		pass
	def draw():
		img = activeClip.grabFrame()
		#TODO draw img
		
class ClipManager():
	class GraphNode:
		def __init__(self,xml):
			self.xml = xml
			#considering parsing xml data to native datatypes for slightly improved performance
			pass 
		def getProperty(prop):
			try: return self.xml.getAttribute(prop)
			except: return ""
		def getNext(state):
			"""
			returns id of next node if transition is to take place, returns -1 otherwise
			"""
			#TODO decide how you want ot handle state information
			pass
	def __init__(self):
		pass
	def load(filename):
		"""
		filename is location of graph xml data file.
		graph xml data file will contain information concerning clips
		"""
		self.graphxml = minidom.parse(filename).getChild()
		self.clipxml = minidom.parse(self.graphxml.getAttribute("clipxml")
		#setup transition graph
		self.graphmap = dict()
		for i in utils.xml.getChildren(self.graphxml.,"clip"):
			self.graphmap[i.getAttribute("id")] = GraphNode(i)
		#set up clipmap
		self.clipmap = dict()
		for i in self.clipxml.childNodes:
			if i:	#check if node is right type and check if name is correct
				type = i.getAttribute("type")
				clip = getAttr(Vclip,type)(i)
				self.clipmap[i.getAttribute("name")] = clip
				
class Overlayer:
	def __init__(self):
		pass
	def update():
		pass
	def draw():
		pass
		