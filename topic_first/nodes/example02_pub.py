#! /usr/bin/env python
import rospy
from std_msgs.msg import String

def fun():
    pass

if __name__ == '__main__':
    rospy.init_node('sample02_pub')
    pub = rospy.Publisher('hello', String, queue_size=10)

    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        str = "sample 02 publisher : %s " % rospy.get_time()
        pub.publish(str)
        rate.sleep()
    pass