import unittest
import os
import sys
import solutions.iterPower as iterPower

class iterPowerTestSquare(unittest.TestCase):
  def test(self):
    self.assertEqual(iterPower.iterPower(2, 2), 4)

class iterPowerTestCube(unittest.TestCase):
  def test(self):
    self.assertEqual(iterPower.iterPower(3, 3), 27)

class iterPowerTestTo4(unittest.TestCase):
  def test(self):
    self.assertEqual(iterPower.iterPower(2, 4), 16)

class iterPowerTestTo4(unittest.TestCase):
  def test(self):
    self.assertEqual(iterPower.iterPower(2.5, 5), 97.65625)

class iterPowerTest0(unittest.TestCase):
  def test(self):
    self.assertEqual(iterPower.iterPower(2.5, 0), 1)

class iterPowerTestFirst(unittest.TestCase):
  def test(self):
    self.assertEqual(iterPower.iterPower(2.5, 1), 2.5)