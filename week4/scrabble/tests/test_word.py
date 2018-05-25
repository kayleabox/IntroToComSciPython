import os
import sys
import unittest

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))

from Word import Word

class WordTest(unittest.TestCase):
  def test(self):
    self.assertEqual(True, True)


# Word.get()
class WordGetTest1(unittest.TestCase):
  def test(self):
    word = Word('name')
    self.assertEqual(word.get(), 'name')

class WordGetTest2(unittest.TestCase):
  def test(self):
    word = Word('supercalifragilisticexpialidoscious')
    self.assertEqual(word.get(), 'supercalifragilisticexpialidoscious')

class WordGetTest3(unittest.TestCase):
  def test(self):
    word = Word('excellent')
    self.assertEqual(word.get(), 'excellent')


# Word.check_hand()
class CheckHandTest1(unittest.TestCase):
  def test(self):
    word = Word('yes')
    hand = {'y': 2, 'c': 1, 'e': 2, 's': 3}
    self.assertEqual(word.check_hand(hand), None)

class CheckHandTest2(unittest.TestCase):
  def test(self):
    word = Word('soup')
    hand = {'y': 2, 'c': 1, 'e': 2, 's': 3}
    self.assertEqual(word.check_hand(hand), False)

class CheckHandTest3(unittest.TestCase):
  def test(self):
    hand = {'r': 1, 'a': 3, 'p': 2, 't': 1, 'u':2}
    word = Word('honey')
    self.assertEqual(word.check_hand(hand), False)

class CheckHandTest4(unittest.TestCase):
  def test(self):
    hand = {'e':1, 'v':2, 'n':1, 'i':1, 'l':2}
    word = Word('evil')
    self.assertEqual(word.check_hand(hand), None)

class CheckHandTest5(unittest.TestCase):
  def test(self):
    hand = {'e':1, 'v':2, 'n':1, 'i':1, 'l':2}
    word = Word('4547')
    self.assertEqual(word.check_hand(hand), False)

class CheckHandTest6(unittest.TestCase):
  def test(self):
    hand = {'e':1, 'v':2, 'n':1, 'i':1, 'l':2}
    word = Word('evvni')
    self.assertEqual(word.check_hand(hand), None)

# word.is_valid
class IsValidWordTest1(unittest.TestCase):
  def test(self):
    word = Word('yes')
    hand = {'y': 2, 'c': 1, 'e': 2, 's': 3}
    self.assertEqual(word.is_valid(hand), True)

class IsValidWordTest2(unittest.TestCase):
  def test(self):
    word = Word('soup')
    hand = {'y': 2, 'c': 1, 'e': 2, 's': 3}
    self.assertEqual(word.is_valid(hand), False)

class IsValidWordTest3(unittest.TestCase):
  def test(self):
    hand = {'r': 1, 'a': 3, 'p': 2, 't': 1, 'u':2}
    word = Word('honey')
    self.assertEqual(word.is_valid(hand), False)

class IsValidWordTest4(unittest.TestCase):
  def test(self):
    hand = {'e':1, 'v':2, 'n':1, 'i':1, 'l':2}
    word = Word('evil')
    self.assertEqual(word.is_valid(hand), True)

class IsValidWordTest5(unittest.TestCase):
  def test(self):
    hand = {'e':1, 'v':2, 'n':1, 'i':1, 'l':2}
    word = Word('')
    self.assertEqual(word.is_valid(hand), False)

class IsValidWordTest6(unittest.TestCase):
  def test(self):
    hand = {'e':1, 'v':2, 'n':1, 'i':1, 'l':2}
    word = Word('evvni')
    self.assertEqual(word.is_valid(hand), False)

class IsValidWordTest7(unittest.TestCase):
  def test(self):
    hand = {'e':1, 'v':2, 'n':1, 'i':1, 'l':2}
    word = Word('3435')
    self.assertEqual(word.is_valid(hand), False)


# Word.calculate_score()
class WordGetScore1(unittest.TestCase):
  def test(self):
    word = Word('hello')
    self.assertEqual(word.calculate_score(7), 40)

class WordGetScore2(unittest.TestCase):
  def test(self):
    word = Word('hello')
    self.assertEqual(word.calculate_score(5), 90)

class WordGetScore3(unittest.TestCase):
  def test(self):
    word = Word('zebra')
    self.assertEqual(word.calculate_score(7), 80)

class WordGetScore4(unittest.TestCase):
  def test(self):
    word = Word('')
    self.assertEqual(word.calculate_score(7), 0)

class WordGetScore5(unittest.TestCase):
  def test(self):
    word = Word('zebra')
    self.assertEqual(word.calculate_score(4), 80)


# Word.calculate_base_score()
class WordCalculateBaseScore1(unittest.TestCase):
  def test(self):
    word = Word('zebra')
    self.assertEqual(word.calculate_base_score(), 80)

class WordCalculateBaseScore2(unittest.TestCase):
  def test(self):
    word = Word('hello')
    self.assertEqual(word.calculate_base_score(), 40)

class WordCalculateBaseScore3(unittest.TestCase):
  def test(self):
    word = Word('')
    self.assertEqual(word.calculate_base_score(), 0)


# Word.add_bonus()
class WordAddBonus1(unittest.TestCase):
  def test(self):
    word = Word('hello')
    base_score = word.calculate_base_score()
    self.assertEqual(word.add_bonus(base_score, 7),  40)

class WordAddBonus2(unittest.TestCase):
  def test(self):
    word = Word('hello')
    base_score = word.calculate_base_score()
    self.assertEqual(word.add_bonus(base_score, 5),  90)

class WordAddBonus3(unittest.TestCase):
  def test(self):
    word = Word('stuff')
    base_score = word.calculate_base_score()
    self.assertEqual(word.add_bonus(base_score, 7),  55)

class WordAddBonus4(unittest.TestCase):
  def test(self):
    word = Word('stuff')
    base_score = word.calculate_base_score()
    self.assertEqual(word.add_bonus(base_score, 5),  105)

