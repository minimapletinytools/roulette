import os
import shutil

folder = "/home/user/stalls/kitchen/faucet01/roulette/src/data/player/handinout/"
output = "/home/user/stalls/kitchen/faucet01/roulette/src/data/player/handinout/handin_backup/"
prefix = "handin"
outprefix = "handin" 
suffix = ".png"
zeros = 5

#find files
for i in range(1,18):
    shutil.copyfile(folder+prefix+str(i).zfill(zeros)+suffix,output+prefix+str(i-1).zfill(zeros)+suffix)
    #reversing
    #shutil.copyfile(folder+prefix+str(i).zfill(zeros)+suffix,output+outprefix+str(16 - (i-1)).zfill(zeros)+suffix)
    