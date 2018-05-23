class Score():
  def __init__(self):
    self.total_score = 0
    self.round_score = 0

  def calculate_word_score(self, word, hand_size):
    self.round_score = word.get_word_score(hand_size)
    self.total_score += self.round_score
    self.print_word_score(word)

  def print_word_score(self, word):
    print('" ' + word.word + ' " earned ' + str(self.round_score) 
    + ' points for that word! Your new score is ' + str(self.total_score))

  def reset(self):
    self.total_score = 0
    self.round_score = 0