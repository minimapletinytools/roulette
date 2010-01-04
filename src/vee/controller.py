import clip
import utils
import xml
from xml.dom import minidom
from pyglet import resource
import utils
class Controller:
	"""
	controller may as well be renamed as state, controller handles all state information, by default, it seems controller comes with a clip manager
	maybe it would be better if we could insert plugins into controller and plugins get controlled automatically by the state machine
	"""
	def __init__(self,exml):
		self.man = ClipManager(utils.getChild(exml,"stage"),self)
		#set up state vars
		self.state = dict()
		for e in [f for f in utils.getChild(exml,"vars").childNodes if f.nodeType == xml.dom.Node.TEXT_NODE]:
			for g in e.data.split():
				self.state[g] = False
	def update(self):
		self.man.update()
	def draw(self):
		self.man.draw()
		
import drawer
import logic
class ClipManager():
	class GraphNode:
		def __init__(self,xml,clip):
			self.clip = clip
			#MAYDO you should really preload some commanly used thing like id.
			self.xml = xml
			self.statelist = list()
			for e in utils.getChildren(self.xml,"next"):
				self.statelist.append((e.getAttribute("id"),e.getAttribute("interval"),utils.getTextNode(e).data))
			#self.statelist.reverse()
		def getAttribute(self,prop):
			try: return self.xml.getAttribute(prop)
			except: return ""
		def getNext(self,state):
			"""
			returns id of next node if transition is to take place, returns -1 otherwise
			"""
			#TODO add interval check into this
			finished = self.clip.isFinished()
			for e,f,g in self.statelist:
				if (not f and finished) or False:   #put intervals check here
					print "evaluating",g.split()
					if logic.evaluate(g,state):
						print "pass"
						return int(e)
			return "-1"
	def __init__(self,xml,parent):
		self.p = parent
		self.active = "1"
		self.load(xml)
	def load(self,node):
		"""
		filename is location of graph xml data file.
		graph xml data file will contain information concerning clips
		"""
		self.graphxml = node
		self.clipxml = minidom.parse(resource.file(self.graphxml.getAttribute("clipxml"))).documentElement
		#set up clipmap
		self.clipmap = dict()
		for i in utils.getChildren(self.clipxml,"clip"):
			type = i.getAttribute("type")
			c = getattr(clip,type,clip.DummyClip)(i)
			self.clipmap[i.getAttribute("name")] = c
		#setup transition graph
		self.graphmap = dict()
		for e in utils.getChildren(self.graphxml,"clipnode"):
			self.graphmap[e.getAttribute("id")] = self.GraphNode(e,self.clipmap[e.getAttribute("clip")])
			
		self.getActiveClip().play()
	def update(self):
		"""
		determine if we need to move around in the clip graph at all
		"""
		new = str(self.graphmap[(self.active)].getNext(self.p.state))
		if new != "-1":
			self.getActiveClip().stop()
			self.active = new
			print "switched to",new
			self.getActiveClip().play()
	def draw(self):
		drawer.draw(self.getActiveClip().grabFrame(),50,50)
	def getActiveClip(self):
		return self.clipmap[self.graphmap[(self.active)].getAttribute("clip")]
				
class Overlayer:
	def __init__(self):
		pass
	def update():
		pass
	def draw():
		pass
		
