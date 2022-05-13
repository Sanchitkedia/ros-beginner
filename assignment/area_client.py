#!/usr/bin/env python

import sys
import rospy
from ros_essentials_cpp.srv import AreaRect
from ros_essentials_cpp.srv import AreaRectRequest
from ros_essentials_cpp.srv import AreaRectResponse

def area_client(x, y):
    rospy.wait_for_service('area_server')
    try:
        area_rect = rospy.ServiceProxy('area_server', AreaRect)
        resp1 = area_rect(x, y)
        return resp1.area
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

def usage():
    return "%s [x y]"%sys.argv[0]

if __name__ == "__main__":
    if len(sys.argv) == 3:
        x = float(sys.argv[1])
        y = float(sys.argv[2])
    else:
        print usage()
        sys.exit(1)
    print "Requesting %f+%f"%(x, y)
    s = area_client(x, y)
    print "%f + %f = %f"%(x, y, s)