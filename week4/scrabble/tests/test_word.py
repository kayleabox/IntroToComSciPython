import os
import sys
import unittest

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))

from Word import Word

class WordTest(unittest.TestCase):
  def test(self):
    self.assertEqual(True, True)

class IsValidWordTest1(unittest.TestCase):
  def test(self):
    word = Word('yes')
    hand = {'y': 2, 'c': 1, 'e': 2, 's': 3}
    self.assertEqual(word.is_valid_word(hand), True)

class IsValidWordTest2(unittest.TestCase):
  def test(self):
    word = Word('soup')
    hand = {'y': 2, 'c': 1, 'e': 2, 's': 3}
    self.assertEqual(word.is_valid_word(hand), False)

class IsValidWordTest3(unittest.TestCase):
  def test(self):
    hand = {'r': 1, 'a': 3, 'p': 2, 't': 1, 'u':2}
    word = Word('honey')
    self.assertEqual(word.is_valid_word(hand), False)

class IsValidWordTest4(unittest.TestCase):
  def test(self):
    hand = {'e':1, 'v':2, 'n':1, 'i':1, 'l':2}
    word = Word('evil')
    self.assertEqual(word.is_valid_word(hand), True)

class IsValidWordTest5(unittest.TestCase):
  def test(self):
    hand = {'e':1, 'v':2, 'n':1, 'i':1, 'l':2}
    word = Word('')
    self.assertEqual(word.is_valid_word(hand), False)

class IsValidWordTest6(unittest.TestCase):
  def test(self):
    hand = {'e':1, 'v':2, 'n':1, 'i':1, 'l':2}
    word = Word('evvni')
    self.assertEqual(word.is_valid_word(hand), False)