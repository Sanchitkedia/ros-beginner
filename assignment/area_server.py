#!/usr/bin/env python

from ros_essentials_cpp.srv import AreaRect
from ros_essentials_cpp.srv import AreaRectRequest
from ros_essentials_cpp.srv import AreaRectResponse

import rospy

def handle_area(req):
    print "Returning [%f + %f = %f]"%(req.a, req.b, (req.a * req.b))
    return AreaRectResponse(req.a * req.b)

def area_server():
    rospy.init_node('area_server')
    s = rospy.Service('area_server', AreaRect, handle_area)
    print "Ready to calculate area."
    rospy.spin()
    
if __name__ == "__main__":
    area_server()