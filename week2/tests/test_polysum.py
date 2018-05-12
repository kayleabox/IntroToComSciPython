import os
import sys
import unittest

from solutions.polysum import polysum

class PolysumTest1(unittest.TestCase):
  def test(self):
    self.assertEqual(polysum(3, 4), 150.9282)

class PolysumTest2(unittest.TestCase):
  def test(self):
    self.assertEqual(polysum(5, 4), 427.5276)

class PolysumTest3(unittest.TestCase):
  def test(self):
    self.assertEqual(polysum(10, 6), 3876.9915)

print(polysum(58, 37))