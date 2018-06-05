class Score():
  def __init__(self):
    self.total_score = 0
    self.round_score = 0

  def get_total(self):
    return self.total_score

  def set_total(self, score):
    self.total_score = score

  def get_round(self):
    return self.round_score

  def set_round(self, score):
    self.round_score = score

  def calculate(self, word, hand_size):
    self.set_round(word.calculate_score(hand_size))
    self.set_total(self.get_total() + self.get_round())
    self.display(word)

  def display(self, word):
    print('" ' + word.word + ' " earned ' + str(self.get_round()) 
    + ' points for that word! Your new score is ' + str(self.get_total()))

  def reset(self):
    self.set_total(0)
    self.set_round(0)