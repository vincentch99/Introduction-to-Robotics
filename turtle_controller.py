#!/usr/bin/env python
# The line above tells Linux that this file is a Python script, and that the OS
# should use the Python interpreter in /usr/bin/env to run it. Don't forget to
# use "chmod +x [filename]" to make this script executable.

# Import the rospy package. For an import to work, it must be specified
# in both the package manifest AND the Python file in which it is used.
import rospy
from geometry_msgs.msg import Twist

#import twist
#make linear & angular from msg
#if and else --> key == w --> result
import sys



# Import the String message type from the /msg directory of the std_msgs package.
from std_msgs.msg import String

# Define the method which contains the node's main functionality
def talker():

    # Create an instance of the rospy.Publisher object which we can  use to
    # publish messages to a topic. This publisher publishes messages of type
    # std_msgs/String to the topic /chatter_talk

    name = sys.argv[1]

    pub = rospy.Publisher(name + '/cmd_vel', Twist, queue_size=10)
    
    # Create a timer object that will sleep long enough to result in a 10Hz
    # publishing rate
    r = rospy.Rate(10) # 10hz

    # Loop until the node is killed with Ctrl-C
    while not rospy.is_shutdown():
        # Construct a string that we want to publish (in Python, the "%"
        # operator functions similarly to sprintf in C or MATLAB)

        T = Twist()
        i = input('Press a key:')

        if i == 'l':
            T.linear.x = 3
        elif i == 'j':
            T.linear.x = -3
        elif i == 'i':
            T.linear.y = 3
        elif i == 'k':
            T.linear.y = -3
        elif i == 'u':
            T.angular.z = 3                      
        elif i == 'o':
            T.angular.z = -3           
  
        
        # Publish our string to the 'chatter_talk' topic
        pub.publish(T)
        print(T)
        
        # Use our rate object to sleep until it is time to publish again
        r.sleep()
            
# This is Python's syntax for a main() method, which is run by default when
# exectued in the shell
if __name__ == '__main__':

    # Run this program as a new node in the ROS computation graph called /talker.
    rospy.init_node('talker', anonymous=True)

    # Check if the node has received a signal to shut down. If not, run the
    # talker method.
    try:
        talker()
    except rospy.ROSInterruptException: pass

