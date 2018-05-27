import os
import sys
import unittest

from solutions.biggest import biggest

class BiggestTest1(unittest.TestCase):
  def test(self):
    animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati'], 'd': ['donkey', 'dog', 'dingo'] }
    self.assertEqual(biggest(animals), 'd')
    
class BiggestTest2(unittest.TestCase):
  def test(self):
    dictionary = {}
    self.assertEqual(biggest(dictionary), None)