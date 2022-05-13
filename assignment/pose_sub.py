#!/usr/bin/env python
import rospy
from turtlesim.msg import Pose

def PoseCallback(message):
    print "pose callback"
    print ('X Co-ordinate = {}'.format(message.x)) 
    print ('Y Co-ordinate = {}' .format(message.y)) 
    print ('Angle = {}'.format(message.theta)) 
    print ('Linear = {}'.format(message.linear_velocity)) 
    print ('Angular = {}'.format(message.angular_velocity)) 

def pose_pub():
    rospy.init_node('pose_pub', anonymous=True)
    rospy.Subscriber("/turtle1/pose", Pose, PoseCallback)
    rospy.spin()

if __name__ == '__main__':
    
 try:
     rospy.loginfo("node initiated.")
     pose_pub()
 except rospy.ROSInterruptException:
     rospy.loginfo("node terminated.")