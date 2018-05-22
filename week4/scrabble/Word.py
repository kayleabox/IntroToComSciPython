from load_words import load_words

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

WORD_LIST = load_words()

class Word():
  def __init__(self, word):
    self.word_list = WORD_LIST
    self.word = word
    self.score = 0
  
  def get_word_score(self, hand_size):
    for letter in self.word:
      self.score = self.score + SCRABBLE_LETTER_VALUES[letter]
    self.score *= len(self.word)
    if len(self.word) == hand_size: 
      self.score += 50
    return self.score

  def is_valid_word(self, hand):
    if self.word == '': 
      return False
    letters_in_word = self.create_letter_dict()
    for key in letters_in_word:
      if key not in hand or hand[key] < letters_in_word[key]: 
        return False
    return self.word in self.word_list

  def create_letter_dict(self):
      letters_in_word = {}
      for letter in self.word:
          if letter not in letters_in_word: 
              letters_in_word[letter] = 1
          else: 
              letters_in_word[letter] += 1
      return letters_in_word
