from load_words import load_words

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1,
    'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8,
    'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1,
    'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1,
    'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4,
    'z': 10
}
WORD_LIST = load_words()

class Word():
  def __init__(self, word = ''):
    self.word = word
    self.score = 0
  
  def get_word(self):
    return self.word

  def get_word_score(self, hand_size):
    self.calculate_base_score()
    self.add_bonus(hand_size)
    return self.score

  def calculate_base_score(self):
    for letter in self.word:
      self.score += SCRABBLE_LETTER_VALUES[letter]    
    self.score *= len(self.word)
    
  def add_bonus(self, hand_size):
    if len(self.word) == hand_size: 
      self.score += 50

  def is_valid_word(self, hand):
    if self.word != '':
      if self.check_word_in_hand(hand) != False:
        return self.word in WORD_LIST
    return False

  def check_word_in_hand(self, hand):
    for letter in self.word:
      if letter not in hand or hand[letter] < self.word.count(letter): 
        return False