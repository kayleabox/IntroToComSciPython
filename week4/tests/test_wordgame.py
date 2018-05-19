import os
import sys
import unittest

from ProblemSet4.load_words import load_words
from ProblemSet4.ps4a import getWordScore
from ProblemSet4.ps4a import updateHand
from ProblemSet4.ps4a import isValidWord


class GetWordScore1(unittest.TestCase):
  def test(self):
    self.assertEqual(getWordScore('soup', 4), 74)

class GetWordScore2(unittest.TestCase):
  def test(self):
    self.assertEqual(getWordScore('soup', 5), 24)

class GetWordScore3(unittest.TestCase):
  def test(self):
    self.assertEqual(getWordScore('argentina', 9), 140)

class GetWordScore4(unittest.TestCase):
  def test(self):
    self.assertEqual(getWordScore('argentina', 11), 90)

class GetWordScore5(unittest.TestCase):
  def test(self):
    self.assertEqual(getWordScore('quick', 5), 150)

class GetWordScore6(unittest.TestCase):
  def test(self):
    self.assertEqual(getWordScore('quick', 6), 100)


class UpdateHand1(unittest.TestCase):
  def test(self):
    self.assertEqual(updateHand({'z': 1, 't': 2, 'l': 1, 'e': 4, 'p': 1, 'h': 2, 'o': 1, 'n': 1}, 'telephone'), {'z': 1, 't': 1, 'l': 0, 'e': 1, 'p': 0, 'h': 1, 'o': 0, 'n': 0})

class UpdateHand2(unittest.TestCase):
  def test(self):
    self.assertEqual(updateHand({'z': 1, 't': 2, 'l': 1, 'e': 4, 'p': 1, 'h': 2, 'o': 1, 'n': 1}, 'nope'), {'z': 1, 't': 2, 'l': 1, 'e': 3, 'p': 0, 'h': 2, 'o': 0, 'n': 0})

class UpdateHand3(unittest.TestCase):
  def test(self):
    self.assertEqual(updateHand({'y': 2, 'c': 1, 'e': 2, 's': 3}, 'yes'), {'y': 1, 'c': 1, 'e': 1, 's': 2})

word_list = load_words()
class WordIsValid1(unittest.TestCase):
  def test(self):
    word = 'yes'
    hand = {'y': 2, 'c': 1, 'e': 2, 's': 3}
    self.assertEqual(isValidWord(word, hand, word_list), True)

class WordIsValid2(unittest.TestCase):
  def test(self):
    word = 'soup'
    hand = {'y': 2, 'c': 1, 'e': 2, 's': 3}
    self.assertEqual(isValidWord(word, hand, word_list), False)

class WordIsValid3(unittest.TestCase):
  def test(self):
    hand = {'r': 1, 'a': 3, 'p': 2, 't': 1, 'u':2}
    word = 'honey'
    self.assertEqual(isValidWord(word, hand, word_list), False)

class WordIsValid3(unittest.TestCase):
  def test(self):
    hand = {'e':1, 'v':2, 'n':1, 'i':1, 'l':2}
    word = 'evil'
    self.assertEqual(isValidWord(word, hand, word_list), True)

class WordIsValid4(unittest.TestCase):
  def test(self):
    hand = {'e':1, 'v':2, 'n':1, 'i':1, 'l':2}
    word = ''
    self.assertEqual(isValidWord(word, hand, word_list), False)

class WordIsValid5(unittest.TestCase):
  def test(self):
    hand = {'e':1, 'v':2, 'n':1, 'i':1, 'l':2}
    word = 'evvni'
    self.assertEqual(isValidWord(word, hand, word_list), False)