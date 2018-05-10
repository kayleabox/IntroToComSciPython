import unittest
import os
import sys
import solutions.gcdRecur as gcdRecur

class gcdRecurTest(unittest.TestCase):
  def test(self):
    self.assertEqual(gcdRecur.gcdRecur(0, 2), 2)

class gcdRecurTest2(unittest.TestCase):
  def test(self):
    self.assertEqual(gcdRecur.gcdRecur(6, 2), 2)

class gcdRecurTest3(unittest.TestCase):
  def test(self):
    self.assertEqual(gcdRecur.gcdRecur(5, 13), 1)

class gcdRecurTest4(unittest.TestCase):
  def test(self):
    self.assertEqual(gcdRecur.gcdRecur(49, 21), 7)

class gcdRecurTest5(unittest.TestCase):
  def test(self):
    self.assertEqual(gcdRecur.gcdRecur(4, 0), 4)

class gcdRecurTest4(unittest.TestCase):
  def test(self):
    self.assertEqual(gcdRecur.gcdRecur(49, -21), 7)