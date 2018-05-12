import os
import sys
import unittest

from solutions.iter_power import iter_power

class IterPowerTestSquare(unittest.TestCase):
  def test(self):
    self.assertEqual(iter_power(2, 2), 4)

class IterPowerTestCube(unittest.TestCase):
  def test(self):
    self.assertEqual(iter_power(3, 3), 27)

class IterPowerTestTo4(unittest.TestCase):
  def test(self):
    self.assertEqual(iter_power(2, 4), 16)

class IterPowerTestTo4(unittest.TestCase):
  def test(self):
    self.assertEqual(iter_power(2.5, 5), 97.65625)

class IterPowerTest0(unittest.TestCase):
  def test(self):
    self.assertEqual(iter_power(2.5, 0), 1)

class IterPowerTestFirst(unittest.TestCase):
  def test(self):
    self.assertEqual(iter_power(2.5, 1), 2.5)