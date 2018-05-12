import os
import sys
import unittest

from solutions.square_num import square, fourth_power

class Square2Test(unittest.TestCase):
    def test(self):
        self.assertEqual(square(2), 4)

class Square3Test(unittest.TestCase):
    def test(self):
        self.assertEqual(square(3), 9)

class Square10Test(unittest.TestCase):
    def test(self):
        self.assertEqual(square(10), 100)

class SquareNegativeTest(unittest.TestCase):
    def test(self):
        self.assertEqual(square(-3), 9)

class Raise2ToTheFourthTest(unittest.TestCase):
    def test(self):
        self.assertEqual(fourth_power(2), 16)

class Raise5ToTheFourthTest(unittest.TestCase):
    def test(self):
        self.assertEqual(fourth_power(5), 625)

class Raise11ToTheFourthTest(unittest.TestCase):
    def test(self):
        self.assertEqual(fourth_power(11), 14641)

