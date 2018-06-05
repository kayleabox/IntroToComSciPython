from hand import Hand

class Game(): 
  def __init__(self):
    self.hand = Hand()
    self.status = 'n'
    self.status_dict = {'n': self.play_new_hand, 'r': self.replay_hand, 'e': self.exit}

  def set_hand(self, new_hand):
    self.hand = new_hand

  def get_status(self): 
    return self.status

  def set_status(self, new_status):
    if new_status in self.get_status_dict():
      self.status = new_status
    else:
      self.set_status(self.get_status_from_user('invalid input. select "n", "r" or "e"'))
    
  def get_status_from_user(self, input_message):
    return input(input_message)

  def get_status_dict(self):
    return self.status_dict.copy()

  def start(self):
    self.set_status(self.get_status_from_user('for a new game enter "n", to replay the last game enter "r" and to exit enter "e"'))
    if self.get_status() != 'e': 
      self.play()
      self.start()

  def play(self):
    self.status_dict[self.get_status()]()

  def play_new_hand(self):
    self.set_hand(Hand(self.set_handsize()))
    self.hand.play_new()

  def replay_hand(self):
    self.hand.replay()

  def exit(self):
    return

  def set_handsize(self):
    try:
      return int(input('how many letters in a hand? '))
    except: 
      return self.set_handsize()



  