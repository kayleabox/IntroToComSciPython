import random

from Score import Score
from Word import Word

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'

class Hand():
  def __init__(self, hand_size = 7):
    self.hand = {}
    self.hand_size = hand_size
    self.num_vowels = hand_size // 3
    self.score = Score()

  def display_hand(self):
    for letter in self.hand.keys():
      for j in range(self.hand[letter]):
        print(letter,end=" ")
    print()

  def deal_hand(self):      
    self.get_vowels()
    self.get_consonants()

  def get_vowels(self):
    for i in range(self.num_vowels):
      vowel = VOWELS[random.randrange(0,len(VOWELS))]
      self.hand[vowel] = self.hand.get(vowel, 0) + 1

  def get_consonants(self):
    for i in range(self.num_vowels, self.hand_size):    
      consonant = CONSONANTS[random.randrange(0,len(CONSONANTS))]
      self.hand[consonant] = self.hand.get(consonant, 0) + 1

  def update_hand(self, word):
    updated_hand = self.hand.copy()
    for letter in word.word:
      updated_hand[letter] -= 1
    return updated_hand

  def calculate_hand_len():
    number_in_hand = 0
    for key in self.hand: 
      number_in_hand += hand[key]
    return number_in_hand

  def play_hand(self):
    while sum(self.hand.values()) > 0: 
      self.display_hand()
      user_word = Word(input('Please enter a word or "." to indicate that you are finished: '))
      if user_word.word == '.':
        break     
      else:
        if not user_word.is_valid_word(self.hand):
          print('invalid word \n')
        else:
          self.score.calculate_score(user_word, self.hand_size)
          self.hand = self.update_hand(user_word)
                  
    if sum(self.hand.values()) <= 0:
      print('Ran out of letters!')
    print('Total: ' + str(self.score.total_score))
