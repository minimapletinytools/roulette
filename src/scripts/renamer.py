import os
import shutil

folder = "/home/user/stalls/kitchen/faucet01/roulette/src/data/fader/fadein/"
output = "/home/user/stalls/kitchen/faucet01/roulette/src/data/fader/fadeout/"
prefix = "fadein"
outprefix = "fadeout" 

suffix = ".png"
zeros = 5

start = 0
end = 20

#find files
for i in range(start,end):
    #shutil.copyfile(folder+prefix+str(i).zfill(zeros)+suffix,output+outprefix+str(i-start).zfill(zeros)+suffix)
    #reversing
    shutil.copyfile(folder+prefix+str(i).zfill(zeros)+suffix,output+outprefix+str(end - (i-start) -1).zfill(zeros)+suffix)
