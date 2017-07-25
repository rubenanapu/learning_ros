#! /usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from rospy_tutorials.srv import (
    AddTwoInts, AddTwoIntsResponse
)


def add_two_ints_handler(req):
    print("Returning [%s + %s = %s]" % (req.a, req.b, (req.a + req.b)))
    return AddTwoIntsResponse(req.a + req.b)


if __name__ == '__main__':
    rospy.init_node(name='add_two_ints_server')

    service = rospy.Service('add_two_ints', AddTwoInts, add_two_ints_handler)

    rospy.spin()
