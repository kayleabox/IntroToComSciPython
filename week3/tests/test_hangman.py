import os
import sys
import unittest

from solutions.hangman.hangman import is_word_guessed
from solutions.hangman.hangman import get_guessed_word
from solutions.hangman.hangman import get_available_letters

class IsWordGuessedTest1(unittest.TestCase):
  def test(self):
    secretWord = 'word'
    lettersGuessed = ['o', 'r', 'l']
    self.assertEqual(is_word_guessed(secretWord, lettersGuessed), False)

class IsWordGuessedTest2(unittest.TestCase):
  def test(self):
    secretWord = 'word'
    lettersGuessed = ['o', 'r', 'w', 'd', 'l', 'm', 'x']
    self.assertEqual(is_word_guessed(secretWord, lettersGuessed), True)

class IsWordGuessedTest3(unittest.TestCase):
  def test(self):
    secretWord = 'word'
    lettersGuessed = ['o', 'r', 'w', 'd']
    self.assertEqual(is_word_guessed(secretWord, lettersGuessed), True)


class GetGuessedWordTest1(unittest.TestCase):
  def test(self):
    secretWord = 'word'
    lettersGuessed = ['o', 'r', 'l']
    self.assertEqual(get_guessed_word(secretWord, lettersGuessed), '_or_')

class GetGuessedWordTest2(unittest.TestCase):
  def test(self):
    secretWord = 'word'
    lettersGuessed = ['o', 'r', 'w', 'd', 'l', 'm', 'x']
    self.assertEqual(get_guessed_word(secretWord, lettersGuessed), 'word')

class GetGuessedWordTest3(unittest.TestCase):
  def test(self):
    secretWord = 'mississippi'
    lettersGuessed = ['s', 'p', 'l', 'x', 'o']
    self.assertEqual(get_guessed_word(secretWord, lettersGuessed), '__ss_ss_pp_')


class GetAvailableLettersTest1(unittest.TestCase):
  def test(self):
    lettersGuessed = ['o', 'r', 'l']
    self.assertEqual(get_available_letters(lettersGuessed), 'abcdefghijkmnpqstuvwxyz')

class GetAvailableLettersTest2(unittest.TestCase):
  def test(self):
    lettersGuessed = ['o', 'r', 'w', 'd', 'l', 'm', 'x']
    self.assertEqual(get_available_letters(lettersGuessed), 'abcefghijknpqstuvyz')

class GetAvailableLettersTest3(unittest.TestCase):
  def test(self):
    lettersGuessed = ['s', 'p', 'l', 'x', 'o']
    self.assertEqual(get_available_letters(lettersGuessed), 'abcdefghijkmnqrtuvwyz')
