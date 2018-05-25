from Hand import Hand

class Game(): 
  def __init__(self):
    self.hand = None
    self.game_status = 'n'
    self.status_dict = {'n': self.play_new_hand, 'r': self.replay_hand , 'e': self.exit_game}

  def play_game(self):
    while self.game_status != 'e':
      self.game_status = self.get_game_status()
      if self.game_status in self.status_dict: 
        self.status_dict[self.game_status]()
      else: 
        print('invalid input')

  def get_game_status(self):
    return input('for a new game enter "n",'
    + ' to replay the last game enter "r"'
    + ' and to exit enter "e"')

  def play_new_hand(self):
    self.hand = Hand(self.get_hand_size())
    self.hand.play_new_hand()

  def replay_hand(self):
    self.hand.replay_hand()

  def exit_game(self):
    return

  def get_hand_size(self):
    try:
      return int(input('how many letters in a hand? '))
    except: 
      return self.get_hand_size()

game = Game()
#game.play_game()


  