import unittest

from load_words import load_words
#from computer_player import play_computer_hand
from single_player import get_word_score
from single_player import is_valid_word
from single_player import update_hand


class GetWordScore1(unittest.TestCase):
  def test(self):
    self.assertEqual(get_word_score('soup', 4), 74)

class GetWordScore2(unittest.TestCase):
  def test(self):
    self.assertEqual(get_word_score('soup', 5), 24)

class GetWordScore3(unittest.TestCase):
  def test(self):
    self.assertEqual(get_word_score('argentina', 9), 140)

class GetWordScore4(unittest.TestCase):
  def test(self):
    self.assertEqual(get_word_score('argentina', 11), 90)

class GetWordScore5(unittest.TestCase):
  def test(self):
    self.assertEqual(get_word_score('quick', 5), 150)

class GetWordScore6(unittest.TestCase):
  def test(self):
    self.assertEqual(get_word_score('quick', 6), 100)


class UpdateHand1(unittest.TestCase):
  def test(self):
    self.assertEqual(update_hand({'z': 1, 't': 2, 'l': 1, 'e': 4, 'p': 1, 'h': 2, 'o': 1, 'n': 1}, 'telephone'), {'z': 1, 't': 1, 'l': 0, 'e': 1, 'p': 0, 'h': 1, 'o': 0, 'n': 0})

class UpdateHand2(unittest.TestCase):
  def test(self):
    self.assertEqual(update_hand({'z': 1, 't': 2, 'l': 1, 'e': 4, 'p': 1, 'h': 2, 'o': 1, 'n': 1}, 'nope'), {'z': 1, 't': 2, 'l': 1, 'e': 3, 'p': 0, 'h': 2, 'o': 0, 'n': 0})

class UpdateHand3(unittest.TestCase):
  def test(self):
    self.assertEqual(update_hand({'y': 2, 'c': 1, 'e': 2, 's': 3}, 'yes'), {'y': 1, 'c': 1, 'e': 1, 's': 2})

word_list = load_words()
class WordIsValid1(unittest.TestCase):
  def test(self):
    word = 'yes'
    hand = {'y': 2, 'c': 1, 'e': 2, 's': 3}
    self.assertEqual(is_valid_word(word, hand, word_list), True)

class WordIsValid2(unittest.TestCase):
  def test(self):
    word = 'soup'
    hand = {'y': 2, 'c': 1, 'e': 2, 's': 3}
    self.assertEqual(is_valid_word(word, hand, word_list), False)

class WordIsValid3(unittest.TestCase):
  def test(self):
    hand = {'r': 1, 'a': 3, 'p': 2, 't': 1, 'u':2}
    word = 'honey'
    self.assertEqual(is_valid_word(word, hand, word_list), False)

class WordIsValid4(unittest.TestCase):
  def test(self):
    hand = {'e':1, 'v':2, 'n':1, 'i':1, 'l':2}
    word = 'evil'
    self.assertEqual(is_valid_word(word, hand, word_list), True)

class WordIsValid5(unittest.TestCase):
  def test(self):
    hand = {'e':1, 'v':2, 'n':1, 'i':1, 'l':2}
    word = ''
    self.assertEqual(is_valid_word(word, hand, word_list), False)

class WordIsValid6(unittest.TestCase):
  def test(self):
    hand = {'e':1, 'v':2, 'n':1, 'i':1, 'l':2}
    word = 'evvni'
    self.assertEqual(is_valid_word(word, hand, word_list), False)
    
'''play_computer_hand({'a': 2, 'm': 1}, word_list, 3)
play_computer_hand({'a': 2, 'm': 1, 't': 1, 'u': 1, 'r': 1, 'e': 1}, word_list, 7)
play_computer_hand({'a': 1, 'i': 1, 'y': 1, 'k': 1, 's': 1, 'x': 2}, word_list, 7)
#" axis " score 44
play_computer_hand({'o': 1, 'a': 1, 'g': 1, 'q': 1, 'b': 1, 'w': 1, 'j': 1}, word_list, 7)
#" jaw " score 39, " bog " score 18 total 57
play_computer_hand({'u': 1, 'a': 1, 'm': 1, 'q': 1, 'k': 1, 'd': 1, 'j': 1}, word_list, 7)
#" dumka " score 60
play_computer_hand({'a': 1, 'u': 1, 'r': 1, 'x': 1, 'm': 1, 'b': 1, 'y': 1}, word_list, 7)
#" braxy " score 85 " mu " score 8 total 93
play_computer_hand({'o': 1, 'a': 1, 'h': 1, 'q': 1, 'b': 1, 'w': 1, 'j': 1}, word_list, 7)'''
