import os
import sys
import unittest

from solutions.odd_tuples import odd_tuples

class OddTuplesTest1(unittest.TestCase):
  def test(self):
    self.assertEqual(odd_tuples(('I', 'am', 'a', 'test', 'tuple')), ('I', 'a', 'tuple'))

class OddTuplesTest2(unittest.TestCase):
  def test(self):
    self.assertEqual(odd_tuples(('I', 'love', 'cats', 'they are', 'cute', 'and', 'furry')), ('I', 'cats', 'cute', 'furry'))