#! /usr/bin/env python
import rospy
from geometry_msgs.msg import Twist

def fun_callback(msg):
    pass

if __name__ == '__main__':
    rospy.init_node('simturtle_publisher')
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)

    twist = Twist()

    twist.linear.y = twist.linear.z = 0.0
    twist.angular.x = twist.angular.y = twist.angular.z = 0

    distance = 2
    speed = 1

    twist.linear.x = distance
    current_distance = 0
    while not rospy.is_shutdown():
        time0 = rospy.Time.now().to_sec()
        while current_distance < distance :
            pub.publish(twist)
            time1 = rospy.Time.now().to_sec()
            current_distance = speed * (time1-time0)
            # current_distance = speed * 0.02
        twist.linear.x = 0
        pub.publish(twist)

    # twist.linear.x = -5.0
    # pub.publish(twist)

    # rate = rospy.Rate(10)
    # while not rospy.is_shutdown():
    #     str = "hello publisher : %s " % rospy.get_time()
    #     pub.publish(str)
    #     rate.sleep()
    pass