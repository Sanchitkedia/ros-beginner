#!/usr/bin/env python

import rospy
import math
from geometry_msgs.msg import Twist

def motion_pub():
   
    mpub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
   
    rospy.init_node('motion_pub', anonymous=True)
    
    rate = rospy.Rate(1) 
    i = 0
    while True:
       twist = Twist()
       twist.linear.x = 2.0
       twist.angular.z = 1.0

       mpub.publish(twist)
       rate.sleep()
       i=i+1
       if (i > 7.0):
         break
    twist.linear.x = 0.0
    mpub.publish(twist)

if __name__ == '__main__':
    try:
        motion_pub()
    except rospy.ROSInterruptException:
        pass
