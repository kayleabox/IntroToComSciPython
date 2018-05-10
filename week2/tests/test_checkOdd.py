import unittest
import os
import sys
import solutions.evalQuadratic as evalQuadratic
import solutions.squareANum as squareANum
import solutions.checkOdd as checkOdd

class oddTestWithOdd(unittest.TestCase):
  def test(self):
    self.assertEqual(checkOdd.odd(3), True)

class oddTestWithEven(unittest.TestCase):
  def test(self):
    self.assertEqual(checkOdd.odd(2), False)