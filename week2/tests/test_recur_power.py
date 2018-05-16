import os
import sys
import unittest

from solutions.recur_power import recur_power

class RecurPowerTestSquare(unittest.TestCase):
  def test(self):
    self.assertEqual(recur_power(2, 2), 4)

class RecurPowerTestCube(unittest.TestCase):
  def test(self):
    self.assertEqual(recur_power(3, 3), 27)

class RecurPowerTestTo4(unittest.TestCase):
  def test(self):
    self.assertEqual(recur_power(2, 4), 16)

class RecurPowerTestTo4(unittest.TestCase):
  def test(self):
    self.assertEqual(recur_power(2.5, 5), 97.65625)

class RecurPowerTest0(unittest.TestCase):
  def test(self):
    self.assertEqual(recur_power(2.5, 0), 1)

class RecurPowerTestFirst(unittest.TestCase):
  def test(self):
    self.assertEqual(recur_power(2.5, 1), 2.5)