import io
import os
import sys
import unittest
import unittest.mock

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))

from Hand import Hand

class HandTest(unittest.TestCase):
  def test(self):
    self.assertEqual(True, True)

# Hand.get()
class HandGetTest1(unittest.TestCase):
  def test(self):
    hand = Hand()
    self.assertEqual(isinstance(hand.get(), dict), True)
    self.assertEqual(len(hand.get()), 0)
    self.assertEqual(hand.get(), {})

class HandGetTest2(unittest.TestCase):
  def test(self):
    hand = Hand(6)
    self.assertEqual(isinstance(hand.get(), dict), True)
    self.assertEqual(len(hand.get()), 0)
    self.assertEqual(hand.get(), {})

class HandGetTest3(unittest.TestCase):
  def test(self):
    hand = Hand()
    hand.deal()
    letters_in_hand = sum(hand.get().values())
    print(hand.get())
    self.assertEqual(isinstance(hand.get(), dict), True)
    self.assertEqual(letters_in_hand, 7)

class HandGetTest4(unittest.TestCase):
  def test(self):
    hand = Hand(6)
    hand.deal()
    letters_in_hand = sum(hand.get().values())
    print(hand.get())
    self.assertEqual(isinstance(hand.get(), dict), True)
    self.assertEqual(letters_in_hand, 6)

# Hand.deal()
class HandDealTest1(unittest.TestCase):
  def test(self):
    hand = Hand()
    hand.deal()
    letters_in_hand = sum(hand.get().values())
    self.assertEqual(letters_in_hand, 7)

class HandDealTest2(unittest.TestCase):
  def test(self):
    hand = Hand(6)
    hand.deal()
    letters_in_hand = sum(hand.get().values())
    self.assertEqual(letters_in_hand, 6)

class HandDealTest3(unittest.TestCase):
  def test(self):
    hand = Hand(8)
    hand.deal()
    letters_in_hand = sum(hand.get().values())
    self.assertEqual(letters_in_hand, 8)

class HandDealTest4(unittest.TestCase):
  def test(self):
    hand = Hand(100)
    hand.deal()
    letters_in_hand = sum(hand.get().values())
    self.assertEqual(letters_in_hand, 100)

class HandDealTest5(unittest.TestCase):
  def test(self):
    hand = Hand(0)
    hand.deal()
    letters_in_hand = sum(hand.get().values())
    self.assertEqual(letters_in_hand, 0)


# Hand.display()
class HandDisplayTest(unittest.TestCase):
  @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
  def assert_stdout(self, expected_output, mock_stdout):
    hand = Hand()
    hand.display()
    self.assertEqual(mock_stdout.getvalue().strip('\n'), expected_output)

  def test(self):
    hand = Hand()
    hand.set({'e':1, 'v':2, 'n':1, 'i':1, 'l':2})
    hand.updated_hand = {'e':1, 'v':2, 'n':1, 'i':1, 'l':2}
    #hand.display()
    #self.assert_stdout('e v v n i l l ')
    hand.updated_hand = {'e':1, 'v':2, 'y':1, 'i':1, 'o':2}
    #self.assert_stdout('e v v y i o o')


# Hand.get_vowels()
VOWEL_SET = set(['a', 'e', 'i', 'o', 'u'])
def vowels_test(self, hand_size):
  hand = Hand(hand_size)
  hand.get_vowels()
  number_vowels = sum(hand.get().values())
  expected_number_vowels = hand_size//3
  are_vowels = set(hand.get().keys()) <= VOWEL_SET
  self.assertEqual(number_vowels, expected_number_vowels)
  self.assertEqual(are_vowels, True)

class HandGetVowelsTest1(unittest.TestCase):
  def test(self):
    '''hand = Hand(6)
    hand.get_vowels()
    number_vowels = sum(hand.get()[key] for key in hand.get())
    are_vowels = set(hand.get().keys()) <= VOWEL_SET
    self.assertEqual(number_vowels, 2)
    self.assertEqual((set(hand.get().keys()) <= VOWEL_SET), True)'''
    vowels_test(self, 6)

class HandGetVowelsTest2(unittest.TestCase):
  def test(self):
    '''hand = Hand(9)
    hand.get_vowels()
    number_vowels = sum(hand.get()[key] for key in hand.get())
    are_vowels = set(hand.get().keys()) <= VOWEL_SET
    self.assertEqual(number_vowels, 3)
    self.assertEqual((set(hand.get().keys()) <= VOWEL_SET), True)'''
    vowels_test(self, 9)

class HandGetVowelsTest3(unittest.TestCase):
  def test(self):
    '''hand = Hand(30)
    hand.get_vowels()
    number_vowels = sum(hand.get()[key] for key in hand.get())
    are_vowels = set(hand.get().keys()) <= VOWEL_SET
    self.assertEqual(number_vowels, 10)
    self.assertEqual((set(hand.get().keys()) <= VOWEL_SET), True)'''
    vowels_test(self, 30)

class HandGetVowelsTest4(unittest.TestCase):
  def test(self):
    '''hand = Hand(11)
    hand.get_vowels()
    number_vowels = sum(hand.get()[key] for key in hand.get())
    are_vowels = set(hand.get().keys()) <= VOWEL_SET
    self.assertEqual(number_vowels, 3)
    self.assertEqual((set(hand.get().keys()) <= VOWEL_SET), True)'''
    vowels_test(self, 11)

# Hand.get_consonants()
CONSONANT_SET = set(['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n',
                  'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z'])

def consonant_test(self, hand_size):
  hand = Hand(hand_size)
  hand.get_consonants()
  number_consonants = sum(hand.get().values())
  expected_number_consonants = hand_size - hand_size//3
  are_consonants = set(hand.get().keys()) <= CONSONANT_SET
  self.assertEqual(number_consonants, expected_number_consonants)
  self.assertEqual(are_consonants, True)

class HandGetConsonantsTest1(unittest.TestCase):
  def test(self):
    '''hand = Hand(30)
    hand.get_consonants()
    number_consonants = sum(hand.get()[key] for key in hand.get())
    are_consonants = set(hand.get().keys()) <= CONSONANT_SET
    self.assertEqual(number_consonants, 20)
    self.assertEqual((set(hand.get().keys()) <= CONSONANT_SET), True)'''
    consonant_test(self, 30)

class HandGetConsonantsTest2(unittest.TestCase):
  def test(self):
    '''hand = Hand(5)
    hand.get_consonants()
    number_consonants = sum(hand.get()[key] for key in hand.get())
    are_consonants = set(hand.get().keys()) <= CONSONANT_SET
    self.assertEqual(number_consonants, 4)
    self.assertEqual((set(hand.get().keys()) <= CONSONANT_SET), True)'''
    consonant_test(self, 5)

class HandGetConsonantsTest3(unittest.TestCase):
  def test(self):
    '''hand = Hand(9)
    hand.get_consonants()
    number_consonants = sum(hand.get()[key] for key in hand.get())
    are_consonants = set(hand.get().keys()) <= CONSONANT_SET
    self.assertEqual(number_consonants, 6)
    self.assertEqual((set(hand.get().keys()) <= CONSONANT_SET), True)'''
    consonant_test(self, 9)

class HandGetConsonantsTest4(unittest.TestCase):
  def test(self):
    '''hand = Hand(11)
    hand.get_consonants()
    number_consonants = sum(hand.get()[key] for key in hand.get())
    are_consonants = set(hand.get().keys()) <= CONSONANT_SET
    self.assertEqual(number_consonants, 8)
    self.assertEqual((set(hand.get().keys()) <= CONSONANT_SET), True)'''
    consonant_test(self, 11)

# Hand.calculate_len()
class CalculateHandLenTest1(unittest.TestCase):
  def test(self):
    hand = Hand()
    hand.set({'e':1, 'v':2, 'n':1, 'i':1, 'l':2})
    self.assertEqual(hand.calculate_len(), 7)

class CalculateHandLenTest2(unittest.TestCase):
  def test(self):
    hand = Hand(15)
    hand.set({'e':5, 'v':2, 'n':4, 'i':2, 'l':2})
    self.assertEqual(hand.calculate_len(), 15)

class CalculateHandLenTest3(unittest.TestCase):
  def test(self):
    hand = Hand()
    hand.set({'e':1, 'v':-2, 'n':1, 'i':-1, 'l':2})
    self.assertEqual(hand.calculate_len(), 1)

class CalculateHandLenTest4(unittest.TestCase):
  def test(self):
    hand = Hand()
    self.assertEqual(hand.calculate_len(), 0)


# Hand.play()



# Hand.update()
class HandUpdateTest1(unittest.TestCase):
  def test(self):
    hand = Hand()
    hand.updated_hand = {'e':5, 'v':2, 'n':4, 'i':2, 'l':2}
    hand.update('nvn')
    self.assertEqual(hand.updated_hand, {'e':5, 'v':1, 'n':2, 'i':2, 'l':2})

class HandUpdateTest2(unittest.TestCase):
  def test(self):
    hand = Hand()
    hand.updated_hand = {'x':5, 'v':2, 'n':4, 'i':2, 'l':2}
    hand.update('xnxnvvxxl')
    self.assertEqual(hand.updated_hand, {'x':1, 'v':0, 'n':2, 'i':2, 'l':1})

class HandUpdateTest3(unittest.TestCase):
  def test(self):
    hand = Hand()
    hand.updated_hand = {'x':0, 'v':2, 'n':4, 'i':0, 'l':2}
    hand.update('vnlv')
    self.assertEqual(hand.updated_hand, {'x':0, 'v':0, 'n':3, 'i':0, 'l':1})

  
# Hand.process_userword()



# Hand.evaluate_word()



# Hand.display_total_score()



# Hand.replay()



# Hand.play_new()

