#! /usr/bin/env python
import rospy
from std_msgs.msg import String
import GetChar 
def fun_callback(msg):
    pass

if __name__ == '__main__':
    rospy.init_node('getchar_pub')
    pub = rospy.Publisher('hello', String, queue_size=10)
    rate = rospy.Rate(10)
    kb   = GetChar()
    tw = str()
    while not rospy.is_shutdown():
        ch = kb.getch()

        if   ch == 'w':
            tw.linear.x  =  2.0;    print ("forward")
        elif ch == 's':
            tw.linear.x  = -2.0;    print ("backward")
        elif ch == 'a':
            tw.angular.z =  2.0;    print ("turn left")
        elif ch == 'd':
            tw.angular.z = -2.0;    print ("turn right")
        elif ch == 'Q':             break
        else:                       pass

        # pub.publish(tw)

        rate.sleep()
    pass