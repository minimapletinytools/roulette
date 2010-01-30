import shutil

#folder = "/home/user/Desktop/Link to stalls/kitchen/faucet01/roulette/src/data/jake_FINAL/clips/waitlean/"
#prefix = "waitlean"
#suffix = ".png"
#rstart = 0
#rend = 11
#outputstart = 11
#frames = 100
#reverse = False

#folder = "/home/user/Desktop/Link to stalls/kitchen/faucet01/roulette/src/data/jake_FINAL/clips/leantowait/"
#prefix = "leantowait"
#suffix = ".png"
#rstart = 12
#rend = 19
#outputstart = 19
#frames = 40
#reverse = True

folder = "/home/user/Desktop/Link to stalls/kitchen/faucet01/roulette/src/data/jake_FINAL/clips/Bdies5/"
prefix = "Bdies5"
suffix = ".png"
rstart = 39
rend = 49
outputstart = 49
frames = 200
reverse = True

l = range(rstart,rend)
if reverse: l.reverse()
f = []
while len(f) < frames:
    f.extend(l[0:len(l)-1])
    l.reverse()

for i in range(0,len(f)):
    shutil.copyfile(folder+prefix+str(f[i]).zfill(5)+suffix, folder+prefix+str(outputstart+i).zfill(5)+suffix)
    


l = range(rstart,rend)
f = []
while len(f) < frames:
    f.extend(l[0:len(l)-1])
    l.reverse()

for i in range(0,len(f)):
    shutil.copyfile(folder+prefix+str(f[i]).zfill(5)+suffix, folder+prefix+str(outputstart+i).zfill(5)+suffix)
    

