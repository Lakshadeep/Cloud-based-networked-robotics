#include "opencv2/highgui/highgui.hpp"
#include "opencv2/imgproc/imgproc.hpp"
#include <iostream>
#include <stdio.h>

using namespace cv;
int thresh = 24;
int max_thresh = 255;
RNG rng(12345);

/** @function main */
int main(int argc, char** argv)
{
  // std::cout << "Success1" << std::endl;
  Mat src, src_gray;

  /// Read the image
  src = imread("outimage.jpg", 1 );
  //std::cout << "Success2" << std::endl;
  if( !src.data )
    { return -1; }
  //std::cout << "Success3" << std::endl;
  /// Convert it to gray
  cvtColor( src, src_gray, CV_BGR2GRAY );

  Mat canny_output;
  vector<vector<Point> > contours;
  vector<Vec4i> hierarchy;

  /// Detect edges using canny
  Canny( src_gray, canny_output, thresh, thresh*2, 3 );
  /// Find contours
  findContours( canny_output, contours, hierarchy, CV_RETR_TREE, CV_CHAIN_APPROX_SIMPLE, Point(0, 0) );


  return contours.size();
}
