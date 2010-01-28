import xml.dom.minidom
import os

directory = "/media/windows/stuff/kitchen/faucet01/posterizeme/videos"
videofolder = "videos/jake_FINAL/"
outputfolder = "jake_FINAL/clips/"
soundfolder = "jake_FINAL/sound/"
type = "CachedImageClip"
width, height = "320","240"
suffix = ".png"
soundsuffix = ".aiff"
duration = ""
frames = ""
durinms = 90
#<clip name="FSFH2_3" videoname="videos/jake/FH2_3.mov" folder="jake_clips/FH2_3/" prefix="FH2_3" sound="jake_sound/FH2_3.aiff" durinms="90" type="CachedImageClip" width="320" height="240" frames="58" duration="5.2200003"/>

def stripext(fn):
    x = len(fn)
    for i in range(1,x+1):
        if fn[x-i] == '.':
            return fn[0:i]
def getext(fn):
    x = len(fn)
    for i in range(1,x+1):
        if fn[x-i] == '.':
            return fn[x-i+1:x]
            
for e in os.listdir(directory):
    if getext(e) != "mov":
        continue
    f = stripext(e)
    y = xml.dom.minidom.parseString("<clip />").childNodes[0]
    attr = dict()
    attr["name"] = f
    attr["videoname"] = videofolder+e
    attr["durinms"] = durinms
    attr["type"] = type
    attr["width"],attr["height"] = width,height
    attr["folder"] = outputfolder + f
    attr["sound"] = soundfolder + f + soundsuffix
    attr["prefix"] = f
    
    #not needed
    attr["suffix"] = suffix
    attr["duration"] = duration
    attr["frames"] = frames
    for i in attr.keys():
        y.setAttribute(i,str(attr[i]))
    print y.toprettyxml()