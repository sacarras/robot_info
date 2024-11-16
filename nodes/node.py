#!/usr/bin/python3
# -*- coding: utf-8 -*-

import rospy
from robot_info.robotinfo import Robotinfo 
# If you discomment in the Cmakelist.txt this line catkin_python_setup() and you add to the package the file setup.py, you can import the class and you don't need the PYTHONPATH

if __name__ == '__main__':
    try:
        # Variable for the node name
        name_node = "robot_info" # Name of the node is robot_info
        # Start the node
        rospy.init_node(name_node)
        # Print information in the terminal
        rospy.loginfo("Node %s has started", name_node)
        # Call the class that has all the code
        node = Robotinfo()
        # Create and spin the node
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
