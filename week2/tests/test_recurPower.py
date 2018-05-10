import unittest
import os
import sys
import solutions.recurPower as recurPower

class recurPowerTestSquare(unittest.TestCase):
  def test(self):
    self.assertEqual(recurPower.recurPower(2, 2), 4)

class recurPowerTestCube(unittest.TestCase):
  def test(self):
    self.assertEqual(recurPower.recurPower(3, 3), 27)

class recurPowerTestTo4(unittest.TestCase):
  def test(self):
    self.assertEqual(recurPower.recurPower(2, 4), 16)

class recurPowerTestTo4(unittest.TestCase):
  def test(self):
    self.assertEqual(recurPower.recurPower(2.5, 5), 97.65625)

class recurPowerTest0(unittest.TestCase):
  def test(self):
    self.assertEqual(recurPower.recurPower(2.5, 0), 1)

class recurPowerTestFirst(unittest.TestCase):
  def test(self):
    self.assertEqual(recurPower.recurPower(2.5, 1), 2.5)