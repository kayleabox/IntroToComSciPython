import unittest
import os
import sys
import solutions.gcdIter as gcdIter
        

class gcdIterTest(unittest.TestCase):
  def test(self):
    self.assertEqual(gcdIter.gcdIter(1, 3), 1)

class gcdIterTest2(unittest.TestCase):
  def test(self):
    self.assertEqual(gcdIter.gcdIter(6, 3), 3)

class gcdIterTest3(unittest.TestCase):
  def test(self):
    self.assertEqual(gcdIter.gcdIter(21, 49), 7)

class gcdIterTest4(unittest.TestCase):
  def test(self):
    self.assertEqual(gcdIter.gcdIter(9, 7), 1)

class gcdIterTest5(unittest.TestCase):
  def test(self):
    self.assertEqual(gcdIter.gcdIter(9, 0), 1)