import os
import sys
import unittest

from solutions.gcd_recur import gcd_recur

class GcdRecurTest(unittest.TestCase):
  def test(self):
    self.assertEqual(gcd_recur(0, 2), 2)

class GcdRecurTest2(unittest.TestCase):
  def test(self):
    self.assertEqual(gcd_recur(6, 2), 2)

class GcdRecurTest3(unittest.TestCase):
  def test(self):
    self.assertEqual(gcd_recur(5, 13), 1)

class GcdRecurTest4(unittest.TestCase):
  def test(self):
    self.assertEqual(gcd_recur(49, 21), 7)

class GcdRecurTest5(unittest.TestCase):
  def test(self):
    self.assertEqual(gcd_recur(4, 0), 4)

class GcdRecurTest4(unittest.TestCase):
  def test(self):
    self.assertEqual(gcd_recur(49, -21), 7)