#! /usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from std_msgs.msg import String


def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)


class Listener(object):
    def __init__(self):
        rospy.init_node('listener', anonymous=True)

        rospy.Subscriber("chatter", String, callback)

        # spin() simply keeps python from exiting until this node is stopped
        rospy.spin()


if __name__ == '__main__':
    Listener()
