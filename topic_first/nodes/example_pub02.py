#! /usr/bin/env python

import rospy
from std_msgs.msg import String

global pub
def fun_callback(msg):
    rospy.loginfo('%s',msg.data)

    global pub
    str = "add publisher : %s " % rospy.get_time()
    pub.publish(str)

    return

if __name__ == '__main__':
    rospy.init_node('sample_sub')
    pub = rospy.Publisher('hello02', String, queue_size=10)

    rospy.Subscriber('hello', String, callback=fun_callback)
    rospy.spin()

    pass