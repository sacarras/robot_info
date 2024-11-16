#!/usr/bin/python3
# -*- coding: utf-8 -*-

import rospy
#Import the class that has all the code
from robot_info.robotinfosub import RobotInfoSub

if __name__ == '__main__':
    try:
        # Start the node that calls robotinfosub
        rospy.init_node("robotinfosub")
        rospy.logdebug("Node robotinfosub has started")

        # Create and spin the node
        # Call the class that has all the code
        node = RobotInfoSub()

        rospy.spin()
    except rospy.ROSInterruptException:
        pass
