from Hand import Hand

class Game(): 
  def __init__(self):
    self.hand = None
    self.status = 'n'
    self.status_dict = {'n': self.play_new_hand, 'r': self.replay_hand , 'e': self.exit}

  def get_status(self): 
    return self.status

  def set_status(self):
    self.status = input('for a new game enter "n",'
    + ' to replay the last game enter "r"'
    + ' and to exit enter "e"')

  def get_status_dict(self):
    return self.status_dict.copy()

  def start(self):
    self.set_status()
    if self.get_status() != 'e': 
      self.play()
      self.start()

  def play(self):
      if self.get_status() in self.get_status_dict(): 
        self.status_dict[self.get_status()]()
      else: 
        print('invalid input')

  def play_new_hand(self):
    self.hand = Hand(self.set_hand_size())
    self.hand.play_new()

  def replay_hand(self):
    self.hand.replay()

  def exit(self):
    return

  def set_hand_size(self):
    try:
      return int(input('how many letters in a hand? '))
    except: 
      return self.set_hand_size()



  