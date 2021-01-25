project(depth2png)

cmake_minimum_required(VERSION 3.18)

#

# OpenCV
# SET(OpenCV_DIR "/usr/local/Cellar/opencv@2/2.4.13.7_3/share/OpenCV")
# find_package( OpenCV 2.4 REQUIRED )
# SET(OpenCV_DIR "/usr/local/Cellar/opencv@3/3.4.10_4/share/OpenCV")
find_package( OpenCV 3 REQUIRED )
include_directories( ${OpenCV_INCLUDE_DIRS} )
link_directories(${OpenCV_LIB_DIR})



ADD_EXECUTABLE( depth2png depth2png.cpp) 
TARGET_LINK_LIBRARIES( depth2png ${OpenCV_LIBS} )

