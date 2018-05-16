import os
import sys
import unittest

from solutions.check_odd import odd

class OddTestWithOdd(unittest.TestCase):
  def test(self):
    self.assertEqual(odd(3), True)

class OddTestWithEven(unittest.TestCase):
  def test(self):
    self.assertEqual(odd(2), False)