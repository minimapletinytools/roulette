import os
import shutil

folder = "/home/user/Desktop/Link to stalls/kitchen/faucet01/roulette/src/data/jake_FINAL/clips/leantowait/"
output = "/home/user/Desktop/Link to stalls/kitchen/faucet01/roulette/src/data/jake_FINAL/clips/leantowait/"
prefix = "SH1_1"
outprefix = "leantowait" 

suffix = ".png"
zeros = 5

start = 0
end = 19

#find files
for i in range(start,end):
    #shutil.copyfile(folder+prefix+str(i).zfill(zeros)+suffix,output+outprefix+str(i-start).zfill(zeros)+suffix)
    #reversing
    shutil.copyfile(folder+prefix+str(i).zfill(zeros)+suffix,output+outprefix+str(end - (i-start) -1).zfill(zeros)+suffix)