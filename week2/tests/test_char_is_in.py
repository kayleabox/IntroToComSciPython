import os
import sys
import unittest

from solutions.char_is_in import is_in

class IsInTest1(unittest.TestCase):
  def test(self):
    self.assertEqual(is_in('z', 'abz'), True)

class IsInTest2(unittest.TestCase):
  def test(self):
    self.assertEqual(is_in('a', 'abc'), True)

class IsInTest3(unittest.TestCase):
  def test(self):
    self.assertEqual(is_in('a', 'bcghjk'), False)

class IsInTest4(unittest.TestCase):
  def test(self):
    self.assertEqual(is_in('j', 'bcghjk'), True)

class IsInTest5(unittest.TestCase):
  def test(self):
    self.assertEqual(is_in('i', 'abcghjrstwxy'), False)

class IsInTest6(unittest.TestCase):
  def test(self):
    self.assertEqual(is_in('x', 'abcghjrstwxy'), True)

class IsInTest7(unittest.TestCase):
  def test(self):
    self.assertEqual(is_in('i', ''), False)
