#!/bin/bash 
# pip install pandas
# sudo apt install ffmpeg

imgToRos_dir='/Users/jin/Q_Mac/work/pre_iphoneData/imgToRos' 
# ros_workspace='/home/jin/catkin_ws'
depth2png_dir='/Users/jin/Q_Mac/work/pre_iphoneData/depth2png/build/depth2png'
frame_num=$(wc -l < Frames.txt)
alias python3=/Library/Frameworks/Python.framework/Versions/3.9/bin/python3.9

cp Frames.txt frame_timestamps.txt
python $imgToRos_dir/rgbd.py $(pwd)
# python $imgToRos_dir/image.py $(pwd)
# python $imgToRos_dir/imu.py 
python $imgToRos_dir/sync-data_org.py $(pwd)
mkdir color
cd color
# index should start from 1 (very important!!!)
ffmpeg -i ../Frames.m4v %d.png
cd ..
mkdir depth
cd depth
# change your depth format in depth2png.cpp 16bit png or .exr
$depth2png_dir/depth2png ../FramesDpt.depth $frame_num
# cd .. 
# # force to 640X480
# $ros_workspace/devel/lib/img_pub/bag_compress $(pwd) mybag.bag
# rosbag info mybag.bag