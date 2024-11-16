#!/usr/bin/python3
# -*- coding: utf-8 -*-

import roslib
import rospy
import rospkg
from std_msgs.msg import String,Int64
from robotinfo_msgs.msg import Robotinfomsg # Import the custom msg
from robot_info.srv import Addtwoints, Robotinfoservice # Import the custom srv

class RobotInfoSub(object):
    def __init__(self):
        """
        Init method.
        You need to declare here all of the variables of your code.
        """
        # Class variables

        #self.__sub = rospy.Subscriber("name_topic", msgtype, self.callback)
            # Name of the topic: name_topic
            # Type of the msg: - rostopic info /name_topic
            #                   It is a msgtype
            # Callback function = callback()

        self.__sub1 = rospy.Subscriber("topic_string_example", String, self.callback_string)
            # Name of the topic: topic_string_example
            # Type of the msg: - rostopic info /topic_string_example
            #                   It is a String
            # Callback function = callback_string()

        self.__sub2 = rospy.Subscriber("topic_int_example", Int64, self.callback_int)
            # Name of the topic: topic_int_example
            # Type of the msg: - rostopic info /topic_int_example
            #                   It is a Int64
            # Callback function = callback_string()        
        
        self.__sub3 = rospy.Subscriber("topic_custom_example", Robotinfomsg, self.robot_info)
            # Name of the topic: topic_custom_example
            # Type of the msg: - rostopic info /topic_custom_example
            #                   It is a Robotinfomsg
            # Callback function = robot_info() 

        # Create a client for the service robot_info_battery
        self.__srv_client = rospy.ServiceProxy("robot_info_battery", Robotinfoservice)
        #Start the code of the node
        self.main()

    def main (self):

        rospy.loginfo(" Hello I'm a subscriber..." )
        
        # Use the client for the service robot_info_battery
        rospy.logwarn("Client service:  ")
        battery_mini = self.__srv_client.call("Mini")
        rospy.loginfo(" The service returned this battery valor: [%s] for Mini", str(battery_mini))


    def callback_string(self, msg):
        # msg type is a string
        rospy.loginfo(" Hello I'm the string subscriber callback..." )
        rospy.loginfo(" The data recived is [%s]", msg)
        rospy.loginfo(" The data recived is [%s]", msg.data)

    def callback_int(self, msg):
        # msg type is a Int64
        rospy.loginfo(" Hello I'm the int subscriber callback..." )
        rospy.loginfo(" The data recived is [%s]", str(msg))

    def robot_info(self, msg):
        # msg type is a Robotinfomsg
        rospy.loginfo(" Hello" )
        rospy.loginfo(" The data is [%s]", str(msg))
        rospy.loginfo(" The name of the robot is [%s]", msg.robot)

