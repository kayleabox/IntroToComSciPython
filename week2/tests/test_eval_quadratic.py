import os
import sys
import unittest

from solutions.eval_quadratic import eval_quadratic

class EvalQuadraticTest(unittest.TestCase):
  def test(self):
    self.assertEqual(eval_quadratic(2, 3, 4, 5), 69)
