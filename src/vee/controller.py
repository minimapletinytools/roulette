import clip
import utils
import xml
from xml.dom import minidom
from pyglet import resource
import utils
import drawer
import graph
import time

#TODO add image wheel if things start slowing down since you are loading 3 images each frame
class Controller:
	"""
	controller may as well be renamed as state, controller handles all state information, by default, it seems controller comes with a clip manager
	maybe it would be better if we could insert plugins into controller and plugins get controlled automatically by the state machine
	"""
	def __init__(self,exml):
		#set up state vars
		self.exml = exml
		self.resetStates()
	
	def resetStates(self):
		self.man = ClipManager(utils.getChildWithAttribute(self.exml,"stage","name","brandon"),self)
		self.eyes = ClipManager(utils.getChildWithAttribute(self.exml,"stage","name","eyes"),self)
		self.player = ClipManager(utils.getChildWithAttribute(self.exml,"stage","name","player"),self)
		self.state = dict()
		for e in [f for f in utils.getChild(self.exml,"vars").childNodes if f.nodeType == xml.dom.Node.TEXT_NODE]:
			for g in e.data.split():
				self.state[g] = 0
		graph.init_graph(self.state)
	def update(self):
		self.man.update()
		self.player.update()
		self.eyes.update()
		if "RESET" in self.state:
			self.resetStates()
	def draw(self):
		self.man.draw()
		self.player.draw()
		self.eyes.draw()
	def press(self):
		#these should be passed into graph.py instead
		if not self.state["press"]:
			self.state["time_pressed"] = time.time()
			self.state["press"] = True 
	def release(self,dt):
		self.state["press"] = False		

class ClipManager():
	def __init__(self,xml,parent):
		self.p = parent
		self.active = "start"
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
			c.preload(False,True)
			self.clipmap[i.getAttribute("name")] = c
		#setup transition graph
		self.graphmap = dict()
		for e in utils.getChildren(self.graphxml,"clipnode"):
			if e.getAttribute("id") == "1":
				self.active = e.getAttribute("name")
			self.graphmap[e.getAttribute("name")] = GraphNode(e,self.clipmap[e.getAttribute("clip")])
		
		self.getActiveClip().play()
	def update(self):
		"""
		determine if we need to move around in the clip graph at all
		"""
		new = str(self.graphmap[(self.active)].getNext(self.p.state))
		if new != "-1":
			#if the frame is indeed a new one (i.e. we are not looping or frozen)
			if new != self.active:
				graph.on_new_frame(self.p.state)
			self.getActiveClip().stop()
			self.active = new
			print "switched to",new
			self.getActiveClip().play()
	def draw(self):
		drawer.draw(self.getActiveClip().grabFrame(),0,0)
	def getActiveClip(self):
		return self.clipmap[self.graphmap[(self.active)].getAttribute("clip")]
				
class GraphNode:
	def __init__(self,xml,clip):
		self.clip = clip
		#MAYDO you should really preload some commanly used thing like id.
		self.xml = xml
		
		#===================================================================
		# self.statelist = list()
		# for e in utils.getChildren(self.xml,"next"):
		#	self.statelist.append((e.getAttribute("id"),e.getAttribute("interval"),utils.getTextNode(e).data))
		#===================================================================
	def getAttribute(self,prop):
		try: return self.xml.getAttribute(prop)
		except: return ""
	def getNext(self,state):
		"""
		returns id of next node if transition is to take place, returns -1 otherwise
		new version is tricky, uses statemap.py
		"""
		return getattr(graph,"graph_"+self.xml.getAttribute("name"),graph.graph_default)(state,self.clip)
	def getNextOLD(self,state):
		"""
		returns id of next node if transition is to take place, returns -1 otherwise
		old version uses the logic system
		"""
		#TODO add interval check into this
		finished = self.clip.isFinished()
		for e,f,g in self.statelist:
			if (not f and finished) or False:   #TODO put intervals check here
				print "evaluating",g.split()
				if logic.evaluate(g,state):
					print "pass"
					return int(e)
		return "-1"