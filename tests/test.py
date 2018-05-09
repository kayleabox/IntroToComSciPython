import unittest
import os
import sys
import evalQuadratic
import squareANum
import oddCheck

def fun(x):
    return x + 1

class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(fun(3), 4)

class evalQuadraticTest(unittest.TestCase):
  def test(self):
    self.assertEqual(evalQuadratic.evalQuadratic(2, 3, 4, 5), 69)

class squareANumTest(unittest.TestCase):
    def test(self):
        self.assertEqual(squareANum.square(3), 9)

class oddTestWithOdd(unittest.TestCase):
  def test(self):
    self.assertEqual(oddCheck.odd(3), True)

class oddTestWithEven(unittest.TestCase):
  def test(self):
    self.assertEqual(oddCheck.odd(2), False)
