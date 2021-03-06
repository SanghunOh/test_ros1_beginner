#! /usr/bin/env python
import rospy
from std_msgs.msg import String

def fun_callback(msg):
    rospy.loginfo('%s',msg.data)
    pass

if __name__ == '__main__':
    rospy.init_node('sample_pub')
    pub = rospy.Publisher('hello', String, queue_size=10)

    pub = rospy.Publisher('hello', String, queue_size=10)
    rospy.Subscriber('hello02', String, callback=fun_callback)

    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        str = "hello publisher : %s " % rospy.get_time()
        pub.publish(str)
        rate.sleep()
    pass