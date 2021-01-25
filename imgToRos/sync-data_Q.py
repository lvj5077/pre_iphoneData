# Synchronize the accelerometer and gyroscope data  

import sys
import pandas as pd
import numpy as np

# Read data
G = -9.805
path=sys.argv[1]
if path[-1] != '/' or path[-1] != '\\':
    path = path + '/'
path_accel= path + 'Accel.txt'
acc=( pd.read_csv(path_accel,names=list('tabc')))
ax=G*acc[list('a')].values
ay=G*acc[list('b')].values
az=G*acc[list('c')].values

path_gyro= path + 'Gyro.txt'
gyro=( pd.read_csv(path_gyro,names=list('tabc')))
qx=gyro[list('a')].values
qy=gyro[list('b')].values
qz=gyro[list('c')].values

path_rpy= path + 'RPY.txt'
rpy=( pd.read_csv(path_rpy,names=list('tabc')))
r=rpy[list('a')].values
p=rpy[list('b')].values
y=rpy[list('c')].values

t=acc[list('t')].values

path_gvt= path + 'Gravity.txt'
gvt=( pd.read_csv(path_gvt,names=list('tabc')))
gx=G*gvt[list('a')].values
gy=G*gvt[list('b')].values
gz=G*gvt[list('c')].values




M=np.column_stack((t,ax+gx,ay+gy,az+gz,qx,qy,qz,r,p,y))

path= path + 'imu_vn100.log'
np.savetxt(path, M, delimiter="\t",fmt='%.6f')
