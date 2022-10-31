#!/usr/bin/env python
import numpy as np
import rospy
from turtle_patrol.srv import Patrol  # Import service type
import sys


def patrol_client(turtle):
    # Initialize the client node
    rospy.init_node('{}_patrol_client'.format(turtle))
    # Wait until patrol service is ready
    rospy.wait_for_service('/{}/patrol'.format(turtle))
    try:
        # Acquire service proxy
        patrol_proxy = rospy.ServiceProxy(
            turtle +'/patrol', Patrol)
        vel = 2.0  # Linear velocity
        omega = 1.0  # Angular velocity
        x = 1.0
        y = 1.0
        theta = np.pi 
        rospy.loginfo('Command {} to patrol'.format(turtle))
        # Call patrol service via the proxy
        patrol_proxy(vel, omega, x, y, theta)
    except rospy.ServiceException as e:
        rospy.loginfo(e)


if __name__ == '__main__':
    patrol_client(sys.argv[1])

