import os
import shutil

folder = "/home/user/stalls/kitchen/faucet01/roulette/src/data/player/handinout/"
output = "/home/user/stalls/kitchen/faucet01/roulette/src/data/player/handinout/handin_backup/"
prefix = "handin"
outprefix = "handin" 

suffix = ".png"
zeros = 5

start = 1
end = 18

#find files
for i in range(start,end):
    shutil.copyfile(folder+prefix+str(i).zfill(zeros)+suffix,output+prefix+str(i-start).zfill(zeros)+suffix)
    #reversing
    #shutil.copyfile(folder+prefix+str(i).zfill(zeros)+suffix,output+outprefix+str(16 - (i-start)).zfill(zeros)+suffix)
