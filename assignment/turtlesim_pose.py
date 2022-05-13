#!/usr/bin/env python

import rospy
from turtlesim.msg import Pose


def poseCallback(pose_message):
    print ("pose callback")
    print ('x = {}'.format(pose_message.x)) 
    print ('y = {}' .format(pose_message.y)) 
    print ('yaw = {}'.format(pose_message.theta)) 


if __name__ == '__main__':
    try:
        
        rospy.init_node('turtlesim_motion_pose', anonymous=True)
        pose_subscriber = rospy.Subscriber("/turtle1/pose", Pose, poseCallback) 
        rospy.spin()
       
    except rospy.ROSInterruptException:
        rospy.loginfo("node terminated.")