import os
import sys
import unittest

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))

from Game import Game

class GameTest(unittest.TestCase):
  def test(self):
    self.assertEqual(True, True)