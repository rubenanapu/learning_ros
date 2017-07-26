#! /usr/bin/env python
# -*- coding: utf-8 -*-

import unittest


class ExampleTestCase(unittest.TestCase):

    def test_sum(self):
        self.assertEquals(1 + 1, 2, 'Sum has a wrong result')


if __name__ == '__main__':

    import rosunit
    rosunit.unitrun('test_example', 'test_example', ExampleTestCase)
