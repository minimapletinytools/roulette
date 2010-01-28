import xml.dom.minidom

name = "fadeout"
prefix = "fadeout"
folder = "fader/fadeout/"
suffix = ".png"
ctype = "CachedImageClip"
frames = 20

durinms = 50


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
