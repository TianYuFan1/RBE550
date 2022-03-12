#!/usr/bin/env python

import rospy

from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

class Navigation:

    def __init__(self):
        # Initialize this node
        rospy.init_node("assist")
        # Subscribers
        rospy.Subscriber("/gopher_presence/base_scan", LaserScan, self.lidar_cb)
        # Publishers 
        self.move_pub = rospy.Publisher("/gopher_presence/base_controller/cmd_vel", Twist, queue_size = 1)
    
    def lidar_cb(self, msg):
        pass
    
    def run(self):
        rospy.spin()

nav = Navigation()
nav.run()
    