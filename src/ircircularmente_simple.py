#! /usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
rospy.init_node('topic_publisher')
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
rate = rospy.Rate(3)
ircircularmente= Twist() # defining the way we can allocate the values
ircircularmente.linear.x = 0.3 # allocating the values in x direction - linear
ircircularmente.angular.z = 1.0  # allocating the values in z direction - angular
while not rospy.is_shutdown():
  pub.publish(ircircularmente)
  rate.sleep()
