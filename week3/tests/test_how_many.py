import os
import sys
import unittest

from solutions.how_many import how_many

class HowManyTest1(unittest.TestCase):
  def test(self):
    animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati'], 'd': ['donkey', 'dog', 'dingo'] }
    self.assertEqual(how_many(animals), 6)

class HowManyTest2(unittest.TestCase):
  def test(self):
    animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati'], 'd': ['donkey', 'dog', 'dingo'], 'e': ['elephant', 'egg'] }
    self.assertEqual(how_many(animals), 8)