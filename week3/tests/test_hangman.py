import os
import sys
import unittest

from solutions.hangman.ps3_hangman import isWordGuessed
from solutions.hangman.ps3_hangman import getGuessedWord
from solutions.hangman.ps3_hangman import getAvailableLetters


class IsWordGuessedTest1(unittest.TestCase):
  def test(self):
    secretWord = 'word'
    lettersGuessed = ['o', 'r', 'l']
    self.assertEqual(isWordGuessed(secretWord, lettersGuessed), False)

class IsWordGuessedTest2(unittest.TestCase):
  def test(self):
    secretWord = 'word'
    lettersGuessed = ['o', 'r', 'w', 'd', 'l', 'm', 'x']
    self.assertEqual(isWordGuessed(secretWord, lettersGuessed), True)

class IsWordGuessedTest3(unittest.TestCase):
  def test(self):
    secretWord = 'word'
    lettersGuessed = ['o', 'r', 'w', 'd']
    self.assertEqual(isWordGuessed(secretWord, lettersGuessed), True)


class GetGuessedWordTest1(unittest.TestCase):
  def test(self):
    secretWord = 'word'
    lettersGuessed = ['o', 'r', 'l']
    self.assertEqual(getGuessedWord(secretWord, lettersGuessed), '_or_')

class GetGuessedWordTest2(unittest.TestCase):
  def test(self):
    secretWord = 'word'
    lettersGuessed = ['o', 'r', 'w', 'd', 'l', 'm', 'x']
    self.assertEqual(getGuessedWord(secretWord, lettersGuessed), 'word')

class GetGuessedWordTest3(unittest.TestCase):
  def test(self):
    secretWord = 'mississippi'
    lettersGuessed = ['s', 'p', 'l', 'x', 'o']
    self.assertEqual(getGuessedWord(secretWord, lettersGuessed), '__ss_ss_pp_')


class GetAvailableLettersTest1(unittest.TestCase):
  def test(self):
    lettersGuessed = ['o', 'r', 'l']
    self.assertEqual(getAvailableLetters(lettersGuessed), 'abcdefghijkmnpqstuvwxyz')

class GetAvailableLettersTest2(unittest.TestCase):
  def test(self):
    lettersGuessed = ['o', 'r', 'w', 'd', 'l', 'm', 'x']
    self.assertEqual(getAvailableLetters(lettersGuessed), 'abcefghijknpqstuvyz')

class GetAvailableLettersTest3(unittest.TestCase):
  def test(self):
    lettersGuessed = ['s', 'p', 'l', 'x', 'o']
    self.assertEqual(getAvailableLetters(lettersGuessed), 'abcdefghijkmnqrtuvwyz')
