import os
import sys
import unittest

from solutions.gcd_iter import gcd_iter

class GcdIterTest(unittest.TestCase):
  def test(self):
    self.assertEqual(gcd_iter(1, 3), 1)

class GcdIterTest2(unittest.TestCase):
  def test(self):
    self.assertEqual(gcd_iter(6, 3), 3)

class GcdIterTest3(unittest.TestCase):
  def test(self):
    self.assertEqual(gcd_iter(21, 49), 7)

class GcdIterTest4(unittest.TestCase):
  def test(self):
    self.assertEqual(gcd_iter(9, 7), 1)

class GcdIterTest5(unittest.TestCase):
  def test(self):
    self.assertEqual(gcd_iter(9, 0), 1)