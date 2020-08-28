#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist

class Rotator():
    def __init__(self):
        self._cmd_vel_publisher = rospy.Publisher('/cmd_vel',Twist, queue_size = 1)
        
    def rotate_forever(self):
        rotate_msg = Twist();
        rotate_msg.angular.z = 0.5
            
        r = rospy.Rate(10)
            
        while not rospy.is_shutdown():
            self._cmd_vel_publisher.publish(rotate_msg)
            rospy.loginfo("Rotating robot %s",rotate_msg)
            r.sleep()

def main():
    rospy.init_node('rotate')
    rotator = Rotator()
    rotator.rotate_forever()
    
if __name__ == "__main__":
    main()