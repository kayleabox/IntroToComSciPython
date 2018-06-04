import random

from Score import Score
from Word import Word

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'

class Hand():
  def __init__(self, hand_size = 7):
    self.hand = {}
    self.updated_hand = {}
    self.hand_size = hand_size
    self.num_vowels = hand_size // 3
    self.score = Score()

  def get(self):
    return self.hand

  def set(self, hand):
    self.hand = hand

  def display(self):
    print(self.get_hand_string())

  def get_hand_string(self):
    return ' '.join([letter for letter in self.updated_hand.keys() for j in range(self.updated_hand[letter])])

  def deal(self):      
    self.get_vowels()
    self.get_consonants()

  def add_letter(self, letter_list, num):
    for i in range(num):
      letter = letter_list[random.randrange(0,len(letter_list))]
      self.hand[letter] = self.hand.get(letter, 0) + 1
  
  def get_vowels(self):
    self.add_letter(VOWELS, self.num_vowels)

  def get_consonants(self):
    self.add_letter(CONSONANTS, self.hand_size - self.num_vowels)

  def update(self, word):
    for letter in word:
      self.updated_hand[letter] -= 1

  def calculate_len(self):
    return sum(self.get().values())

  def play(self):
    self.updated_hand = self.hand.copy() 
    self.get_words_from_user()
    self.display_total_score()

  def get_words_from_user(self):
    while sum(self.updated_hand.values()) > 0: 
      self.display()
      if self.check_user_is_playing(self.set_userword()) == False:
        break

  def set_userword(self):
      return Word(input('Please enter a word or "." to indicate that you are finished: '))

  def check_user_is_playing(self, user_word):
      if user_word.get() == '.':
        return False     
      else:
        self.evaluate_word(user_word)

  def evaluate_word(self, user_word):
    if not user_word.is_valid(self.hand):
      print('invalid word \n')
    else:
      self.score.calculate(user_word, self.hand_size)
      self.update(user_word.get())

  def display_total_score(self):
    if sum(self.updated_hand.values()) <= 0:
      print('Ran out of letters!')
    print('Total: ' + str(self.score.get_total()))

  def replay(self):
    if self.hand != {}:
      self.score.reset()
      self.play()
    else: 
      print('You have not played a hand yet. Please play a new hand first!')

  def play_new(self):
    self.deal()
    self.play()
