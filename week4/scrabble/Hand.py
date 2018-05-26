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
    hand = ''
    for letter in self.updated_hand.keys():
      for j in range(self.updated_hand[letter]):
        hand += letter + ' '
    print(hand)

  def deal(self):      
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

  def update(self, word):
    for letter in word:
      self.updated_hand[letter] -= 1

  def calculate_len(self):
    return sum(self.get().values())

  def play(self):
    self.updated_hand = self.hand.copy()
    while sum(self.updated_hand.values()) > 0: 
      self.display()
      if self.process_userword() == False:
        break
                  
    self.display_total_score()

  def process_userword(self):
      user_word = Word(input('Please enter a word or "." to indicate that you are finished: '))
      if user_word.get() == '.':
        return False     
      else:
        self.evaluate_word(user_word)

  def evaluate_word(self, user_word):
    if not user_word.is_valid(self.hand):
      print('invalid word \n')
    else:
      self.score.calculate_word_score(user_word, self.hand_size)
      self.update(user_word.get())

  def display_total_score(self):
    if sum(self.updated_hand.values()) <= 0:
      print('Ran out of letters!')
    print('Total: ' + str(self.score.total_score))

  def replay(self):
    if self.hand != None:
      self.score.reset()
      self.play()
    else: 
      print('You have not played a hand yet. Please play a new hand first!')

  def play_new(self):
    self.deal()
    self.play()
