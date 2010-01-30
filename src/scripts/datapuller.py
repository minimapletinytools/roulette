import os

folder = "/home/user/roulette/src/data/jake_FINAL/clips/"

for i in os.listdir(folder):
    if os.path.isdir(folder + i):
        try:
            f = folder + i + "/data.txt"
            file = open(f,'r')
            print file.readlines()[1]
        except: pass
