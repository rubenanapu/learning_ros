#! /usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from rospy_tutorials.srv import AddTwoInts


class AddTwoIntsServiceClient(rospy.ServiceProxy):
    """
    NOTE: you don't have to call rospy.init_node() to make calls against
    a service. This is because service clients do not have to be nodes.
    """

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def execute(self):
        # block until the add_two_ints service is available
        # you can optionally specify a timeout
        rospy.wait_for_service('add_two_ints')

        try:
            # Create a handle to the add_two_ints service
            add_two_ints = rospy.ServiceProxy('add_two_ints', AddTwoInts)
            print "Requesting %s + %s" % (self.a, self.b)

            # simplified style
            resp1 = add_two_ints(self.a, self.b)

            if not resp1.sum == (self.a + self.b):
                raise Exception(
                    "test failure, returned sum was %s" % resp1.sum
                )

            return resp1.sum

        except rospy.ServiceException, e:
            "Service call failed: %s", e


if __name__ == '__main__':
    import random

    a = random.randint(-500, 500)
    b = random.randint(-500, 500)

    print "%s + %s = %s" % (a, b, AddTwoIntsServiceClient(a, b).execute())
