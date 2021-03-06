#!/usr/bin/env python

print('xbot begin to move')
import time
import rospy
import std_msgs.msg
from geometry_msgs.msg import Twist
   
def turn_angle():
 pub = rospy.Publisher('/cmd_vel_mux/input/navi', Twist, queue_size=100)

 msg = Twist()
 rotate_vel = float(turn_speed)*3.1416/180
 if "left" is dropdown_direction:
  msg.angular.z = rotate_vel
 else:
  msg.angular.z = -rotate_vel

 rate = rospy.Rate(20)

 start = time.time()

 flag = True
 while not rospy.is_shutdown() and flag:
  sample_time = time.time()
  print((sample_time - start) * rotate_vel , float(turn_degrees)*3.1416/180)
  if ((sample_time - start) * rotate_vel > float(turn_degrees)*3.1416/180):
   flag = False
  pub.publish(msg)
  rate.sleep()

turn_angle() 
