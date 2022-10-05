#! /usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
rospy.init_node('topic_publisher')
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
rate = rospy.Rate(3)
irlinearecta = Twist()
irlinearecta.linear.x = 0.2
while not rospy.is_shutdown():
  pub.publish(irlinearecta)
  rate.sleep()



