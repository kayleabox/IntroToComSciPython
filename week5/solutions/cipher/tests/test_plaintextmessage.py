import os
import sys
import unittest

from PlainTextMessage import PlainTextMessage

class PlainTextMessageGetShiftTest1(unittest.TestCase):
  def test(self):
    message = PlainTextMessage('hello', 2)
    self.assertEquals(message.get_shift(), 2)

class PlainTextMessageGetShiftTest2(unittest.TestCase):
  def test(self):
    message = PlainTextMessage('hello', 5)
    self.assertEquals(message.get_shift(), 5)

class PlainTextMessageGetEncryptingDictTest1(unittest.TestCase):
  def test(self):
    message = PlainTextMessage('hello', 2)
    self.assertEquals(message.get_encrypting_dict(), {'a': 'c', 'b': 'd', 'c': 'e', 'd': 'f', 'e': 'g', 'f': 'h', 'g': 'i', 'h': 'j', 'i': 'k', 'j': 'l', 'k': 'm', 'l': 'n', 'm': 'o', 'n': 'p', 'o': 'q', 'p': 'r', 'q': 's', 'r': 't', 's': 'u', 't': 'v', 'u': 'w', 'v': 'x', 'w': 'y', 'x': 'z', 'y': 'a', 'z': 'b', 'A': 'C', 'B': 'D', 'C': 'E', 'D': 'F', 'E': 'G', 'F': 'H', 'G': 'I', 'H': 'J', 'I': 'K', 'J': 'L', 'K': 'M', 'L': 'N', 'M': 'O', 'N': 'P', 'O': 'Q', 'P': 'R', 'Q': 'S', 'R': 'T', 'S': 'U', 'T': 'V', 'U': 'W', 'V': 'X', 'W': 'Y', 'X': 'Z', 'Y': 'A', 'Z': 'B'})
    self.assertEquals(message.get_encrypting_dict() == message.encrypting_dict, True)
    self.assertEquals(message.get_encrypting_dict() is message.encrypting_dict, False)

class PlainTextMessageGetEncryptingDictTest2(unittest.TestCase):
  def test(self):
    message = PlainTextMessage('hello', 5)
    self.assertEquals(message.get_encrypting_dict(), {'a': 'f', 'b': 'g', 'c': 'h', 'd': 'i', 'e': 'j', 'f': 'k', 'g': 'l', 'h': 'm', 'i': 'n', 'j': 'o', 'k': 'p', 'l': 'q', 'm': 'r', 'n': 's', 'o': 't', 'p': 'u', 'q': 'v', 'r': 'w', 's': 'x', 't': 'y', 'u': 'z', 'v': 'a', 'w': 'b', 'x': 'c', 'y': 'd', 'z': 'e', 'A': 'F', 'B': 'G', 'C': 'H', 'D': 'I', 'E': 'J', 'F': 'K', 'G': 'L', 'H': 'M', 'I': 'N', 'J': 'O', 'K': 'P', 'L': 'Q', 'M': 'R', 'N': 'S', 'O': 'T', 'P': 'U', 'Q': 'V', 'R': 'W', 'S': 'X', 'T': 'Y', 'U': 'Z', 'V': 'A', 'W': 'B', 'X': 'C', 'Y': 'D', 'Z': 'E'})
    self.assertEquals(message.get_encrypting_dict() == message.encrypting_dict, True)
    self.assertEquals(message.get_encrypting_dict() is message.encrypting_dict, False)

class PlainTextMessageGetEncryptedTest1(unittest.TestCase):
  def test(self):
    message = PlainTextMessage('hello', 5)
    self.assertEquals(message.get_message_text_encrypted(), 'mjqqt')

class PlainTextMessageGetEncryptedTest2(unittest.TestCase):
  def test(self):
    message = PlainTextMessage('hello', 2)
    self.assertEquals(message.get_message_text_encrypted(), 'jgnnq')

class PlainTextMessageGetEncryptedTest3(unittest.TestCase):
  def test(self):
    message = PlainTextMessage('Nonsense words: warm knowledge desk proof usual', 24)
    self.assertEquals(message.get_message_text_encrypted(), 'Lmlqclqc umpbq: uypk ilmujcbec bcqi npmmd sqsyj')

class PlainTextMessageChangeShiftTest1(unittest.TestCase):
  def test(self):
    message = PlainTextMessage('hello', 2)
    message.change_shift(5)
    self.assertEquals(message.get_shift(), 5)
    self.assertEquals(message.get_encrypting_dict(), {'a': 'f', 'b': 'g', 'c': 'h', 'd': 'i', 'e': 'j', 'f': 'k', 'g': 'l', 'h': 'm', 'i': 'n', 'j': 'o', 'k': 'p', 'l': 'q', 'm': 'r', 'n': 's', 'o': 't', 'p': 'u', 'q': 'v', 'r': 'w', 's': 'x', 't': 'y', 'u': 'z', 'v': 'a', 'w': 'b', 'x': 'c', 'y': 'd', 'z': 'e', 'A': 'F', 'B': 'G', 'C': 'H', 'D': 'I', 'E': 'J', 'F': 'K', 'G': 'L', 'H': 'M', 'I': 'N', 'J': 'O', 'K': 'P', 'L': 'Q', 'M': 'R', 'N': 'S', 'O': 'T', 'P': 'U', 'Q': 'V', 'R': 'W', 'S': 'X', 'T': 'Y', 'U': 'Z', 'V': 'A', 'W': 'B', 'X': 'C', 'Y': 'D', 'Z': 'E'})
    self.assertEquals(message.get_message_text_encrypted(), 'mjqqt')

class PlainTextMessageChangeShiftTest2(unittest.TestCase):
  def test(self):
    message = PlainTextMessage('hello', 5)
    message.change_shift(2)
    self.assertEquals(message.get_shift(), 2)
    self.assertEquals(message.get_encrypting_dict(), {'a': 'c', 'b': 'd', 'c': 'e', 'd': 'f', 'e': 'g', 'f': 'h', 'g': 'i', 'h': 'j', 'i': 'k', 'j': 'l', 'k': 'm', 'l': 'n', 'm': 'o', 'n': 'p', 'o': 'q', 'p': 'r', 'q': 's', 'r': 't', 's': 'u', 't': 'v', 'u': 'w', 'v': 'x', 'w': 'y', 'x': 'z', 'y': 'a', 'z': 'b', 'A': 'C', 'B': 'D', 'C': 'E', 'D': 'F', 'E': 'G', 'F': 'H', 'G': 'I', 'H': 'J', 'I': 'K', 'J': 'L', 'K': 'M', 'L': 'N', 'M': 'O', 'N': 'P', 'O': 'Q', 'P': 'R', 'Q': 'S', 'R': 'T', 'S': 'U', 'T': 'V', 'U': 'W', 'V': 'X', 'W': 'Y', 'X': 'Z', 'Y': 'A', 'Z': 'B'})
    self.assertEquals(message.get_message_text_encrypted(), 'jgnnq')
