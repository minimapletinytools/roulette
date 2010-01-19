import pygame
import os
import xml.dom.minidom

WORDS = [
("start","Roulette, press button to start"),
("intro","introduction scene"),
("FH1_1","I wonder what it'll feel like..."),
("FH1_2","So you gonna do it?"),
("FH1_3","C'mon man."),
("wait","waiting for player action"),
("FH2_1","What are ya', chicken?"),
("FSFH2_2","Nu Uh. You lost...."),
("FSFH2_3","You said you'd go first."),
("FH3_1","C'mon man, if you're not gonna do it..."),
("FH3_2","Look, i'ts easy..."),
("FH3_3","If you chicken out, I'm gonna..."),
("Bgoesfirst","B decides to take gun and shoot self"),
("waitlean","Brandon stands up impatiently"),
("FH4","Fine, you chicken shit."),
("BshootsY","Brandom points gun at you and shoots"),
("fuckyou","Fuck you"),
("BprepareshootB","Brandon anxiously prepares to shoot self"),
("DH_1","Him against me! Side by Side!"),
("DH_2","Here's to Nick!"),
("DH_3","Call me old fireballs."),
("BshootsB","brandon shoots himself"),
("Bdies","Brandon is dead"),
("youwin","A winner is you"),
("YT_1","your turn"),
("YT_2","now you do it"),
("YT_3","you wont be that lucky"),
("continue","continue #?"),
("youlose","gameover"),
("SH1_1","Again?"),
("SH1_2","I don't want it for you again"),
("SH1_3","after I balled up you gonna pus out"),
("SH2","Fine"),
]

PATH = "words/"
SIZE = (320,240)
FONT_SIZE = 40

pygame.init()
screen = pygame.display.set_mode(SIZE,pygame.DOUBLEBUF)
font = pygame.font.SysFont(pygame.font.get_default_font(), FONT_SIZE)
exml = xml.dom.minidom.parseString("<clips />").getElementsByTagName("clips")[0]
pcode = ""
counter = 1
for i,j in WORDS:
	screen.fill((0,0,0))
	t = font.render(j,False,(255,255,255))
	screen.blit(t,(SIZE[0]/2 - t.get_width()/2,SIZE[1]/2 - t.get_height()/2))
	pygame.display.flip()
	pygame.image.save(screen,os.path.join(PATH,i+"00000.png"))
	time = str(pygame.mixer.Sound(os.path.join("data/sound",i + ".wav")).get_length())
	x = xml.dom.minidom.parseString("<clip name = \"" + i + "\" type=\"ImageClip\" sound = \"" + i +".wav\" durinms = \"10000\" frames = \"1\" duration=\""+time+"\" folder =\"words/\" prefix = \"" + i + "\" />").getElementsByTagName("clip")[0]
	y = xml.dom.minidom.parseString("<clipnode />").childNodes[0]
	y.setAttribute("id",str(counter))
	y.setAttribute("name",i)
	y.setAttribute("clip",i)
	exml.appendChild(y)
	pcode += "def graph_" + i + "(state,clip):\n    if clip.isFinished(): return \"-1\"\n    else: return \"-1\"\n"  
	counter += 1
print exml.toprettyxml()
#print pcode
	