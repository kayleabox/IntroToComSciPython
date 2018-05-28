import os
import sys
import unittest

from CipherTextMessage import CipherTextMessage

class CipherTextMessage1(unittest.TestCase):
  def test(self):
    message = CipherTextMessage('jgnnq')
    self.assertEquals(message.decrypt_message(), (24, 'hello'))

class CipherTextMessageTest2(unittest.TestCase):
  def test(self):
    message = CipherTextMessage('mjqqt')
    self.assertEquals(message.decrypt_message(), (21, 'hello'))

class CipherTextMessageTest3(unittest.TestCase):
  def test(self):
    message = CipherTextMessage('nkrru')
    self.assertEquals(message.decrypt_message(), (20, 'hello'))
  
class CipherTextMessageTest4(unittest.TestCase):
  def test(self):
    message = CipherTextMessage('qnuux')
    self.assertEquals(message.decrypt_message(), (17, 'hello'))

class CipherTextMessageTest5(unittest.TestCase):
  def test(self):
    message = CipherTextMessage('Lmlqclqc umpbq: uypk ilmujcbec bcqi npmmd sqsyj')
    self.assertEquals(message.decrypt_message(), (2, 'Nonsense words: warm knowledge desk proof usual'))
