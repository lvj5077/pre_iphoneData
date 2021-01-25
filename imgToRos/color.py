# Synchronize the accelerometer and gyroscope data  

import sys
import pandas as pd
import numpy as np

# Read data
path=sys.argv[1]
if path[-1] != '/' or path[-1] != '\\':
    path = path + '/'
path_rgb= path + 'Frames.txt'

path_out = path + 'timestamp.txt'

idx=0

with open(path_out, "w") as f_out:
    with open(path_rgb) as f_in:
        line = f_in.readline()
        while line:
            idx=idx+1
            sp = line.split(',')
            f_out.writelines(sp[0]+'\tcolor/'+str(idx)+'.png\t'+'\n')
            line = f_in.readline()
            # line = f_in.readline()
            # line = f_in.readline()