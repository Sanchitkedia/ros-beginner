#!/usr/bin/env python 
import cv2
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

def read_video():
  video_publisher = rospy.Publisher("tennis_ball_image", Image, queue_size=100)
  video_capture = cv2.VideoCapture("video/tennis-ball-video.mp4")
  frame_counter = 0
  while not rospy.is_shutdown():
    ret,rgb_frame = video_capture.read()
    frame_counter += 1
    ros_image = CvBridge().cv2_to_imgmsg(rgb_frame, "bgr8")
    video_publisher.publish(ros_image)
    cv2.waitKey(10)
    if frame_counter == video_capture.get(cv2.CAP_PROP_FRAME_COUNT):
        frame_counter = 0 
        video_capture.set(cv2.CAP_PROP_POS_FRAMES, 0)
  video_capture.release()   

if __name__ == '__main__':

 try:
     rospy.init_node("tennis_ball_publisher", anonymous=True)
     read_video()
     rospy.spin()
 except rospy.ROSInterruptException:
     rospy.loginfo("node terminated.")