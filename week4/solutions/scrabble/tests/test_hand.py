import io
import os
import sys
import unittest
import unittest.mock

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))

from hand import Hand
from score import Score
from word import Word

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


# Hand.get_hand_string()
class HandGetStringTest1(unittest.TestCase):
  def test(self):
    hand = Hand()
    hand.set({'e':1, 'v':2, 'n':1, 'i':1, 'l':2})
    hand.updated_hand = {'e':1, 'v':2, 'n':1, 'i':1, 'l':2}

    self.assertEqual(hand.get_hand_string(), 'e v v n i l l')

class HandGetStringTest2(unittest.TestCase):
  def test(self):
    hand = Hand()
    hand.set({'e':1, 'v':2, 'n':1, 'i':1, 'l':2})
    hand.updated_hand = {'e':4, 'v':2, 'y':1, 'i':1, 'o':3}
    
    self.assertEqual(hand.get_hand_string(), 'e e e e v v y i o o o')


# Hand.display()
class HandDisplayTest1(unittest.TestCase):
  @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
  def assert_stdout(self, expected_output, mock_stdout):
    hand = Hand()
    hand.set({'e':1, 'v':2, 'n':1, 'i':1, 'l':2})
    hand.updated_hand = {'e':1, 'v':2, 'n':1, 'i':1, 'l':2}
    hand.display()
    
    self.assertEqual(mock_stdout.getvalue().strip('\n'), expected_output)

  def test(self):
    self.assert_stdout('e v v n i l l')

class HandDisplayTest2(unittest.TestCase):
  @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
  def assert_stdout(self, expected_output, mock_stdout):
    hand = Hand()
    hand.set({'e':1, 'v':2, 'n':1, 'i':1, 'l':2})
    hand.updated_hand = {'e':4, 'v':2, 'y':1, 'i':1, 'o':3}
    hand.display()
    
    self.assertEqual(mock_stdout.getvalue().strip('\n'), expected_output)
    self.assertEqual(hand.get_hand_string(), 'e e e e v v y i o o o')

  def test(self):
    self.assert_stdout('e e e e v v y i o o o')


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
# need to figure how to mock the game play
class HandPlayTest1(unittest.TestCase):
  @unittest.mock.patch('hand.Hand.set_userword')
  def mock_set_word_function(self, mock_set_word):
    hand = Hand()
    hand.set({'e':1, 'v':2, 'n':1, 'i':1, 'l':2})
    mock_set_word.side_effect = [Word('hi'), Word('evil'), Word('.')]
    hand.play()

    self.assertTrue(mock_set_word.called)

  def test(self):
    self.mock_set_word_function()

class HandPlayTest2(unittest.TestCase):
  @unittest.mock.patch('hand.Hand.get_words_from_user')
  @unittest.mock.patch('hand.Hand.display_total_score')
  def mock_set_word_function(self, mock_get_words_from_user, mock_display_total_score):
    hand = Hand()
    hand.set({'e':1, 'v':2, 'n':1, 'i':1, 'l':2})
    mock_get_words_from_user.side_effect = [None, None, None]
    mock_display_total_score.side_effect = [None, None, None]
    hand.play()

    self.assertTrue(mock_get_words_from_user.called)
    self.assertTrue(mock_display_total_score.called)

  def test(self):
    self.mock_set_word_function()


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

  
# Hand.check_user_is_playing()
class HandCheckUserIsPlayingTest1(unittest.TestCase):
  def test(self):
    hand = Hand()

    self.assertEqual(hand.check_user_is_playing(Word('.')), False)

class HandCheckUserIsPlayingTest2(unittest.TestCase):
  @unittest.mock.patch('hand.Hand.evaluate_word')
  def mock_check_user_is_playing_function(self, mock_evaluate_word):
    hand = Hand()
    hand.set({'e':1, 'v':1, 'n':2, 'i':2, 'l':1})
    hand.updated_hand = {'e':1, 'v':1, 'n':2, 'i':2, 'l':1}
    hand.check_user_is_playing(Word('evil'))

    self.assertTrue(mock_evaluate_word.called)

  def test(self):
    self.mock_check_user_is_playing_function()

class HandCheckUserIsPlayingTest3(unittest.TestCase):
  @unittest.mock.patch('hand.Hand.evaluate_word')
  def mock_check_user_is_playing_function(self, mock_evaluate_word):
    hand = Hand()
    hand.set({'e':1, 'v':1, 'n':2, 'i':2, 'l':1})
    hand.updated_hand = {'e':1, 'v':1, 'n':2, 'i':2, 'l':1}
    hand.check_user_is_playing(Word('soup'))

    self.assertTrue(mock_evaluate_word.called)

  def test(self):
    self.mock_check_user_is_playing_function()


# Hand.evaluate_word()
class HandEvaluateWordTest1(unittest.TestCase):
  @unittest.mock.patch('score.Score.calculate')
  @unittest.mock.patch('hand.Hand.update')
  def mock_evaluate_word_function(self, mock_calculate_score, mock_update_hand):
    hand = Hand()
    hand.set({'e':1, 'v':1, 'n':2, 'i':2, 'l':1})
    hand.updated_hand = {'e':1, 'v':1, 'n':2, 'i':2, 'l':1}
    hand.evaluate_word(Word('evil'))
    
    self.assertTrue(mock_calculate_score.called)
    self.assertTrue(mock_update_hand.called)

  def test(self):
    self.mock_evaluate_word_function()

class HandEvaluateWordTest2(unittest.TestCase):
  @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
  def assert_stdout(self, expected_output, mock_stdout):
    hand = Hand()
    hand.set({'e':1, 'v':1, 'n':2, 'i':2, 'l':1})
    hand.updated_hand = {'e':1, 'v':1, 'n':2, 'i':2, 'l':1}
    hand.evaluate_word(Word('evidfsd'))

    self.assertEqual(mock_stdout.getvalue().strip('\n'), expected_output)

  def test(self):
    self.assert_stdout('invalid word ')
    

# Hand.display_total_score()
class HandDisplayTotalScoreTest1(unittest.TestCase):
  @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
  def assert_stdout(self, expected_output, mock_stdout):
    hand = Hand()
    hand.score.total_score = 20
    hand.display_total_score()

    self.assertEqual(mock_stdout.getvalue().strip('\n'), expected_output)

  def test(self):
    self.assert_stdout('Ran out of letters!\nTotal: 20')

class HandDisplayTotalScoreTest2(unittest.TestCase):
  @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
  def assert_stdout(self, expected_output, mock_stdout):
    hand = Hand()
    hand.score.total_score = 150
    hand.display_total_score()

    self.assertEqual(mock_stdout.getvalue().strip('\n'), expected_output)

  def test(self):
    self.assert_stdout('Ran out of letters!\nTotal: 150')

class HandDisplayTotalScoreTest3(unittest.TestCase):
  @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
  def assert_stdout(self, expected_output, mock_stdout):
    hand = Hand()
    hand.updated_hand = {'f': 1, 'z': 2}
    hand.score.total_score = 10
    hand.display_total_score()

    self.assertEqual(mock_stdout.getvalue().strip('\n'), expected_output)

  def test(self):
    self.assert_stdout('Total: 10')


# Hand.replay()
class HandReplayTest1(unittest.TestCase):
  @unittest.mock.patch('hand.Hand.play')
  @unittest.mock.patch('score.Score.reset')
  def mock_replay_function(self, mock_play, mock_score_reset):
    hand = Hand()
    hand.set({'e':1, 'v':2, 'n':1, 'i':1, 'l':2})
    hand.replay()

    self.assertTrue(mock_score_reset.called)
    self.assertTrue(mock_play.called)

  def test(self):
    self.mock_replay_function()

class HandReplayTest2(unittest.TestCase):
  @unittest.mock.patch('hand.Hand.play')
  @unittest.mock.patch('score.Score.reset')
  def mock_replay_function(self, mock_play, mock_score_reset):
    hand = Hand()
    hand.replay()

    self.assertFalse(mock_score_reset.called)
    self.assertFalse(mock_play.called)

  def test(self):
    self.mock_replay_function()


# Hand.play_new()
class HandPlayNewTest1(unittest.TestCase):
  @unittest.mock.patch('hand.Hand.deal')
  @unittest.mock.patch('hand.Hand.play')
  def mock_play_new_function(self, mock_deal, mock_play):
    hand = Hand()
    hand.set({'e':1, 'v':2, 'n':1, 'i':1, 'l':2})
    hand.play_new()

    self.assertTrue(mock_deal.called)
    self.assertTrue(mock_play.called)

  def test(self):
    self.mock_play_new_function()


