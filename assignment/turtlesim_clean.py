#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math
import time
from std_srvs.srv import Empty

speed=0 
distance=0 
is_forward=0
angular_speed_degree=0
relative_angle_degree=0
desired_angle_degree =0
clockwise=0 
x_goal=0
y_goal=0
x=0
y=0
theta=0
c=0

def PoseCallback(message):
    global x, y, theta
    x = message.x
    y = message.y
    theta = message.theta

def move_input():
        global speed, distance, is_forward
        speed = input('Enter Speed: ')
        distance = input('Enter Distance: ')
        is_forward = input('Motion is Forward ? (Yes = 1,No = 0): ')

def rotate_input():
    global angular_speed_degree, relative_angle_degree, clockwise 
    angular_speed_degree = input('Enter Angular Speed: ')
    relative_angle_degree = input('Enter Angle To Rotate By (Degree): ')
    clockwise = input('Motion is Clockwise ? (Yes = 1,No = 0): ')

def orientation_input():
    global theta,desired_angle_degree
    desired_angle_degree = input('Enter Angle (Degree): ')
    
def go_input():
 global x_goal, y_goal
 x_goal = input('Enter Desired Goal X Co-ordinate: ')
 y_goal = input('Enter Desired Goal Y Co-ordinate: ') 

def move(speed, distance, is_forward):
        
        velocity_message = Twist()
        
  
        if (is_forward):
            velocity_message.linear.x =abs(speed)
        else:
        	velocity_message.linear.x =-abs(speed)

        distance_moved = 0.0
        loop_rate = rospy.Rate(10)  
        velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)

        t0 = rospy.Time.now().to_sec()

        while True :
                rospy.loginfo("The Turtle is Moving")
                velocity_publisher.publish(velocity_message)

                loop_rate.sleep()
                t1 =  rospy.Time.now().to_sec()
                                
                distance_moved = (t1-t0) * speed
                print  distance_moved               
                if  not (distance_moved<distance):
                    rospy.loginfo("Reached")
                    break
        
        velocity_message.linear.x =0
        velocity_publisher.publish(velocity_message)

def rotate (angular_speed_degree,relative_angle_degree,clockwise):
   
    
    velocity_message = Twist()
    
    angular_speed=math.radians(abs(angular_speed_degree))

    if (clockwise):
        velocity_message.angular.z =-abs(angular_speed)
    else:
        velocity_message.angular.z =abs(angular_speed)

    
    loop_rate = rospy.Rate(10)   
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)

    t0 = rospy.Time.now().to_sec()

    while True :
        rospy.loginfo("The Turtle is Rotating")
        velocity_publisher.publish(velocity_message)

        t1 = rospy.Time.now().to_sec()
        current_angle_degree = (t1-t0)*angular_speed_degree
        loop_rate.sleep()

        print 'The current angle is ',current_angle_degree
                       
        if  (current_angle_degree>relative_angle_degree):
            rospy.loginfo("Reached")
            break

    velocity_message.angular.z =0
    velocity_publisher.publish(velocity_message)

def orientation (desired_angle_degree):
    global theta
   
    velocity_message = Twist()
    
    angular_speed_degree = 30
    angular_speed=math.radians(abs(angular_speed_degree))
    relative_angle_radians=((math.radians(abs(desired_angle_degree))) - theta)
    relative_angle_degree=math.degrees(abs(relative_angle_radians))

    if  relative_angle_radians< 0: 
        clockwise = 1
    else:
        clockwise = 0

    if clockwise: 
        velocity_message.angular.z =-abs(angular_speed)
    else:
        velocity_message.angular.z =abs(angular_speed)

    angle_moved = 0.0
    loop_rate = rospy.Rate(10)   
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)

    t0 = rospy.Time.now().to_sec()

    while True :
        rospy.loginfo("The Turtle is Rotating")
        velocity_publisher.publish(velocity_message)

        t1 = rospy.Time.now().to_sec()
        current_angle_degree = (t1-t0)*angular_speed_degree
        loop_rate.sleep()
        print 'current_angle_degree: ',current_angle_degree

        if (current_angle_degree > relative_angle_degree):
            rospy.loginfo("Reached")
            break

    velocity_message.angular.z =0
    velocity_publisher.publish(velocity_message)

def go_to_goal(x_goal, y_goal):
    global x, y, theta
    

    velocity_message = Twist()
    

    while (True):
        K_linear = 0.5 
        distance = abs(math.sqrt(((x_goal-x) ** 2) + ((y_goal-y) ** 2)))

        linear_speed = distance * K_linear

        K_angular = 4.0
        desired_angle_goal = math.atan2(y_goal-y, x_goal-x)
        angular_speed = (desired_angle_goal-theta)*K_angular

        velocity_message.linear.x = linear_speed
        velocity_message.angular.z = angular_speed

        velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
        velocity_publisher.publish(velocity_message)
        
        
        if (distance <0.001):
            print "I have Reached the Co-ordinates: ", x_goal,',', y_goal
            break
 
def grid_clean():
 global theta
 go_to_goal(1.0,1.0)
 orientation(0)

 move(2,9,1)
 time.sleep(1) 
 rotate(10,90,0)
 time.sleep(1)
 move(2,9,1)
 i = 0 
 while not i==6:
       rotate(30,90,0)
       time.sleep(1)
       move(2,1,1)
       rotate(30,90,0)
       time.sleep(1)
       move(2,9,1)

       rotate(30,90,1)
       time.sleep(1)
       move(2,1,1)
       rotate(30,90,1)
       time.sleep(1)
       move(2,9,1)
       i = i + 1

 velocity_message.linear.x = 0
 velocity_message.angular.z = 0
 velocity_publisher.publish(velocity_message)
    
def spiral_clean():
    global x,y
    velocity_message = Twist()
    loop_rate = rospy.Rate(1)
    wk = 4
    rk = 0
    
    while((x<10.5) and (y<10.5)):
        rk=rk+1
        velocity_message.linear.x =rk
        velocity_message.linear.y =0
        velocity_message.linear.z =0
        velocity_message.angular.x = 0
        velocity_message.angular.y = 0
        velocity_message.angular.z =wk
        velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
        velocity_publisher.publish(velocity_message)
        loop_rate.sleep()
 
    velocity_message.linear.x = 0
    velocity_message.angular.z = 0
    velocity_publisher.publish(velocity_message)


if __name__ == '__main__':
    try:
        rospy.init_node('turtlesim_motion_pose', anonymous=True)

        velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
        pose_subscriber = rospy.Subscriber('/turtle1/pose', Pose, PoseCallback) 
        time.sleep(2)
        print "\n *************** Choose The Number You Want To Run ***************"
        c = input ("\n 1.Move \n 2.Rotate \n 3.Orientation \n 4.Go to Goal \n 5.Grid Clean \n 6.Spiral Clean \n")
        if c == 1:
            move_input()
            move(speed, distance, is_forward)    
        elif c == 2:
            rotate_input()
            rotate (angular_speed_degree, relative_angle_degree, clockwise)     
        elif c == 3:
            orientation_input()
            orientation (desired_angle_degree)        
        elif c == 4:
            go_input()
            go_to_goal (x_goal,y_goal)   
        elif c == 5:
            grid_clean()           
        elif c == 6:
            spiral_clean()    
        else:
            print 'Wrong value entered'
            
        
    except rospy.ROSInterruptException:
        rospy.loginfo("node terminated.")