#!/usr/bin/python3
# -*- coding: utf-8 -*-

import roslib
import rospy
import rospkg
import time

from std_msgs.msg import String, Bool, Int64
from robotinfo_msgs.msg import Robotinfomsg # Import the custom msg
from robot_info.srv import Addtwoints, Robotinfoservice # Import the custom srv



class Robotinfo(object):
    def __init__(self):
        """
        Init method.
        You need to declare here all of the variables of your code
        """
        # For declare a Publisher always we use:
            # self.__pub = rospy.Publisher("name_topic", msgtype, queue_size=10) 
            # Name of the topic: name_topic
            # Type of the msg: - rostopic info /name_topic
            #                  - It is a msgtype
            # Queue Size: 10 

        # self.__pub1 is a variable for publish a string
        self.__pub1 = rospy.Publisher("topic_string_example", String, queue_size=10) # Declare a Publisher
            # Name of the topic: topic_string_example
            # Type of the msg: - rostopic info /topic_string_example
            #                  - It is a String
            # Queue Size: 10

        # self.__pub2 is a variable for publish a int
        self.__pub2 = rospy.Publisher("topic_int_example", Int64, queue_size=10) # Declare a Publisher
            # Name of the topic: topic_int_example
            # Type of the msg: - rostopic info /topic_int_example
            #                  - It is a Int64
            # Queue Size: 10

        # self.__pub3 is a variable for publish a custommsg
        self.__pub3 = rospy.Publisher("topic_custom_example", Robotinfomsg, queue_size=10) # Declare a Publisher
            # Name of the topic: topic_custom_example
            # Type of the msg: - rostopic info /topic_custom_example
            #                  - It is a Robotinfomsg
            # Queue Size: 10


        # For declare a Service always we use:
            # self.__srv = rospy.Service("name_srv", srvtype, handle_function) 
            # Name of the Service: name_srv
            # Type of the srv: - rosservice info /name_srv
            #                  - It is a srvtype
            # Callback function = handle_function()

        self.__srv1 = rospy.Service("add_two_ints", Addtwoints, self.handle_addtwoints)
            # Name of the Service: add_two_ints
            # Type of the srv: - rosservice info /add_two_ints
            #                  - It is a Addtwoints
            # Callback function = handle_addtwoints()


        self.__srv2 = rospy.Service("robot_info_battery", Robotinfoservice, self.handle_robot)
            # Name of the Service: robot_info_battery
            # Type of the srv: - rosservice info /robot_info_battery
            #                  - It is a Robotinfoservice
            # Callback function = handle_robot()

        time.sleep(3)
        #Start the code of the node
        self.main()

    def main (self):
        
       self.publish_string() # Call the function that has the method for publish a string
       self.publish_int() # Call the function that has the method for publish a int
       self.publish_custom() # Call the function that has the method for publish a custom msg


    def publish_string(self):

        rospy.logwarn(" Publish a String in the topic: topic_string_example ..." )
        # Publish a String
        name = ""
        name = "Marie" # Variable name is the string
        self.__pub1.publish(name) # Publish the variable name
        rospy.loginfo(" I send the 1 msg: %s" , name )

        self.__pub1.publish("Anto") # Publish the String "Anto"
        rospy.loginfo(" I send the 2 msg: Anto")

        text = "Hello World" # String Variable
        self.__pub1.publish(text) # Use this method to publish a msg in the topic: topic_string_example
        rospy.loginfo(" I send the 3 msg: %s" , text )
        
    def publish_int(self):

        rospy.logwarn(" Publish a Int in the topic: topic_int_example ..." )
        # Publish a Int
        number = 0  # Variable number is the int
        number = 56
        self.__pub2.publish(number) # Publish the variable number
        rospy.loginfo(" I send the msg Int : %s" , str(number) )
    
        self.__pub2.publish(3) # Publish the String "Anto"
        rospy.loginfo(" I send the 2 msg Int: 3")


    def publish_custom(self):

        rospy.logwarn(" Publish a Custom msg in the topic: topic_custom_example ..." )
        # Declare the variable
        robot = Robotinfomsg()
        robot.robot = "Mini" # Custom Msg info
        robot.battery = 45
        self.__pub3.publish(robot) # Publish the variable number
        rospy.loginfo(" I send the msg : %s" , str(robot) )

    def handle_addtwoints(self, req):
        # req is the request data for the Addtwoints srv, in this case we have int64 a and int64 b
        a = req.a
        b = req.b

        # Srv code
        rospy.loginfo(" I recived a : %s" , str(a) )
        rospy.loginfo(" I recived b : %s" , str(b) )
        rospy.loginfo(" Calculating ..." )
        response = a + b
        print(" The service response is:" + str(response))
        return response # Always a srv has a response, in Addtwoints is a Int64 sum

    def handle_robot(self, req):
        # req is the request data for the Robotinfoservice srv, in this case we have a string name
        robot = req.name
        rospy.loginfo(" I recived this name : %s" , robot)
        rospy.loginfo(" Calculating ..." )
        if (robot == "Mini"):
            rospy.loginfo(" The battery is : %s" , str(56)) 
            return 56
        elif (robot == "Tiago"):
            battery = 78
            rospy.loginfo(" The battery is : %s" , str(battery)) 
            return battery
        else:
            rospy.loginfo(" The battery is : %s" , str(0))
            return 0
         # Always a srv has a response, in Robotinfoservice is a Int64 sum

# How we can create a node?
    # Mode 1: Create the node in the folder node and call the class.
        # Mode 1: rosrun robot_config node.py
    # Mode 2 for create a node. In the same file that we have all the code
        # Mode 2: If you use this, you need to discomment the if and run the node with: rosrun robot_config robotinfo.py
""" if __name__ == '__main__':
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
        pass """
