#include "opencv2/highgui/highgui.hpp"
#include "opencv2/imgproc/imgproc.hpp"
#include <iostream>
#include <stdio.h>

using namespace cv;

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

  /// Reduce the noise so we avoid false circle detection
  GaussianBlur( src_gray, src_gray, Size(9, 9), 2, 2 );
  //std::cout << "Success4" << std::endl;
  vector<Vec3f> circles;

  /// Apply the Hough Transform to find the circles
  HoughCircles( src_gray, circles, CV_HOUGH_GRADIENT, 1, src_gray.rows/16, 200, 10, 0, 200 );
/*
  /// Draw the circles detected
  for( size_t i = 0; i < circles.size(); i++ )
  {
      Point center(cvRound(circles[i][0]), cvRound(circles[i][1]));
      int radius = cvRound(circles[i][2]);
       //circle center
      circle( src, center, 3, Scalar(0,255,0), -1, 8, 0 );
       //circle outline
      circle( src, center, radius, Scalar(0,0,255), 3, 8, 0 );
   }

  /// Show your results
  namedWindow( "Hough Circle Transform Demo", CV_WINDOW_AUTOSIZE );
  imshow( "Hough Circle Transform Demo", src );
  */
   //std::cout << "Success" << std::endl;
   //std::cout << circles.size() << std::endl;
  //waitKey(0);
  return circles.size();
}
