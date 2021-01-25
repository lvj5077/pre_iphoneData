# Synchronize the accelerometer and gyroscope data  

import sys
import pandas as pd
import numpy as np

# Read data
path=sys.argv[1]
if path[-1] != '/' or path[-1] != '\\':
    path = path + '/'
path_rgb= path + 'frame_timestamps.txt'

path_out = path + 'Intrinsic.txt'

idx=0

with open(path_out, "w") as f_out:
    with open(path_rgb) as f_in:
        line = f_in.readline()
        while line:
            idx=idx+1
            sp = line.split('\n')
            f_out.writelines(sp[0]+' '+'507.1131 507.6100 321.1179 241.3314'+'\n')
            line = f_in.readline()
            # line = f_in.readline()
            # line = f_in.readline()