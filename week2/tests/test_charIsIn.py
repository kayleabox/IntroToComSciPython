import unittest
import os
import sys
import solutions.charIsIn as charIsIn

class isInTest1(unittest.TestCase):
  def test(self):
    self.assertEqual(charIsIn.isIn('z', 'abz'), True)

class isInTest2(unittest.TestCase):
  def test(self):
    self.assertEqual(charIsIn.isIn('a', 'abc'), True)

class isInTest3(unittest.TestCase):
  def test(self):
    self.assertEqual(charIsIn.isIn('a', 'bcghjk'), False)

class isInTest4(unittest.TestCase):
  def test(self):
    self.assertEqual(charIsIn.isIn('j', 'bcghjk'), True)

class isInTest5(unittest.TestCase):
  def test(self):
    self.assertEqual(charIsIn.isIn('i', 'abcghjrstwxy'), False)

class isInTest6(unittest.TestCase):
  def test(self):
    self.assertEqual(charIsIn.isIn('x', 'abcghjrstwxy'), True)

class isInTest7(unittest.TestCase):
  def test(self):
    self.assertEqual(charIsIn.isIn('i', ''), False)
