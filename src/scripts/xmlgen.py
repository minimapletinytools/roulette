import xml.dom.minidom

name = "fader"
prefix = "handout"
folder = "fader/"
suffix = ".png"
ctype = "CachedImageClip"
frames = 17

durinms = 200


attr = dict()
attr["name"] = name
attr["duration"] = frames*durinms
attr["durinms"] = durinms
attr["type"] = ctype
attr["folder"] = folder
attr["suffix"] = suffix
attr["frames"] = frames 
attr["prefix"] = prefix

x = xml.dom.minidom.parseString("<clip />").childNodes[0]
for i in attr.keys():
    x.setAttribute(i,str(attr[i]))

print x.toprettyxml()
