import os
import string
import sys
import unittest

from Message import Message

class MessageGetTest(unittest.TestCase):
  def test(self):
    message = Message('hi')
    self.assertEquals(message.get_message_text(), 'hi')

class MessageGetWordsTest(unittest.TestCase):
  def test(self):
    message = Message('hi')
    self.assertEquals(message.get_valid_words(), message.valid_words)
    self.assertEquals(message.get_valid_words() is message.valid_words, False)
    self.assertIsInstance(message.get_valid_words(), list)
    
class MessageBuildShiftDictionaryTest(unittest.TestCase):
  def test(self):
    message = Message('hi')
    self.assertEquals(message.build_shift_dict(2), {'a': 'c', 'b': 'd', 'c': 'e', 'd': 'f', 'e': 'g', 'f': 'h', 'g': 'i', 'h': 'j', 'i': 'k', 'j': 'l', 'k': 'm', 'l': 'n', 'm': 'o', 'n': 'p', 'o': 'q', 'p': 'r', 'q': 's', 'r': 't', 's': 'u', 't': 'v', 'u': 'w', 'v': 'x', 'w': 'y', 'x': 'z', 'y': 'a', 'z': 'b', 'A': 'C', 'B': 'D', 'C': 'E', 'D': 'F', 'E': 'G', 'F': 'H', 'G': 'I', 'H': 'J', 'I': 'K', 'J': 'L', 'K': 'M', 'L': 'N', 'M': 'O', 'N': 'P', 'O': 'Q', 'P': 'R', 'Q': 'S', 'R': 'T', 'S': 'U', 'T': 'V', 'U': 'W', 'V': 'X', 'W': 'Y', 'X': 'Z', 'Y': 'A', 'Z': 'B'})
    self.assertIsInstance(message.build_shift_dict(4), dict)
    
class MessageMapAlphabetTest1(unittest.TestCase):
  def test(self):
    message = Message('hi')
    self.assertEquals(message.map_alphabet(string.ascii_lowercase, 2), {'a': 'c', 'b': 'd', 'c': 'e', 'd': 'f', 'e': 'g', 'f': 'h', 'g': 'i', 'h': 'j', 'i': 'k', 'j': 'l', 'k': 'm', 'l': 'n', 'm': 'o', 'n': 'p', 'o': 'q', 'p': 'r', 'q': 's', 'r': 't', 's': 'u', 't': 'v', 'u': 'w', 'v': 'x', 'w': 'y', 'x': 'z', 'y': 'a', 'z': 'b'})
    self.assertIsInstance(message.map_alphabet(string.ascii_lowercase, 2), dict)

class MessageMapAlphabetTest2(unittest.TestCase):
  def test(self):
    message = Message('hi')
    self.assertEquals(message.map_alphabet(string.ascii_uppercase, 2), {'A': 'C', 'B': 'D', 'C': 'E', 'D': 'F', 'E': 'G', 'F': 'H', 'G': 'I', 'H': 'J', 'I': 'K', 'J': 'L', 'K': 'M', 'L': 'N', 'M': 'O', 'N': 'P', 'O': 'Q', 'P': 'R', 'Q': 'S', 'R': 'T', 'S': 'U', 'T': 'V', 'U': 'W', 'V': 'X', 'W': 'Y', 'X': 'Z', 'Y': 'A', 'Z': 'B'})
    self.assertIsInstance(message.map_alphabet(string.ascii_lowercase, 2), dict)

class MessageApplyShiftTest(unittest.TestCase):
  def test(self):
    message = Message('hi')
    self.assertEquals(message.apply_shift(2), 'jk')
    self.assertEquals(message.apply_shift(4), 'lm')
    self.assertEquals(message.apply_shift(8), 'pq')
    self.assertEquals(message.apply_shift(-1), None)
    self.assertEquals(message.apply_shift(26), None)