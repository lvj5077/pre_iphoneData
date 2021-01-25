#include <fstream>
#include <iostream>
#include <limits>
#include <memory>
#include <sstream>
#include "opencv2/opencv.hpp"

#include <iostream>

using namespace cv;

void process(const std::string& depthFile, size_t numDepthFrames, size_t depthWidth = 192, size_t depthHeight = 256) {

  const char *filenamechar = depthFile.c_str();
  FILE *fpr = fopen(filenamechar, "rb");

  int frame = 1;

  while (frame < numDepthFrames) {

    Mat image = Mat::zeros(192, 256, CV_32F);
    float* pData = (float*)image.data;
    for (int i = 0; i < 192*256; i++)
    {
        fread(&pData[i], sizeof(float), 1, fpr);
    }

    Mat image16bit = 1000*image;
    image16bit.convertTo(image16bit, CV_16U);
    const std::string filename = std::to_string(frame) + ".png";

    std::cout << "frame: " << frame<< std::endl;

    imwrite(filename,image16bit);

    frame++;
  }

}


int main(int argc, char* argv[]) {
  if (argc >= 2) {
    std::string depthFile(argv[1]);
    int numDepthFrames = 1;
    if (argc >= 3) {
      numDepthFrames = std::atoi(argv[2]);
    }
    process(depthFile, numDepthFrames);
  } else {
    std::cerr << "Usage: depth2PNG path/to/file.depth [numDepthFrames]" << std::endl;
  }
  return 0;
}