import xml.dom.minidom

name = "player_handout"
prefix = "handout"
folder = "player/jake_clips/handout"
suffix = ".png"
type = "CachedImageClip"
frames = 17

durinms = 200


attr = dict()
attr["name"] = name
attr["duration"] = frames*durinms
attr["durinms"] = durinms
attr["type"] = type
attr["folder"] = folder
attr["suffix"] = suffix
attr["frames"] = frames 
attr["prefix"] = prefix

x = xml.dom.minidom.parseString("<clip />").childNodes[0]
for i in attr.keys():
    x.setAttribute(i,str(attr[i]))

print x.toprettyxml()