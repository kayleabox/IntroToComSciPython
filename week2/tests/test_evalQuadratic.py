import unittest
import os
import sys
import solutions.evalQuadratic as evalQuadratic

class evalQuadraticTest(unittest.TestCase):
  def test(self):
    self.assertEqual(evalQuadratic.evalQuadratic(2, 3, 4, 5), 69)
