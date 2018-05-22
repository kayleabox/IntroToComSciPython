from Hand import Hand
from load_words import load_words
#from players.HumanPlayer import HumanPlayer
#from players.ComputerPlayer import ComputerPlayer

class Game(): 
  def __init__(self, hand_size = 7):
    self.hand_size = hand_size
    self.hand = None
    self.game_status = 'n'
    self.status_dict = {'n': self.play_new_hand, 'r': self.replay_hand , 'e': self.exit_game}

  def play_game(self):
    while self.game_status != 'e':
      self.game_status = input('for a new game enter "n", to replay the last game enter "r"' + 
      ' and to exit enter "e"')
      if self.status_dict[self.game_status]: 
        self.status_dict[self.game_status]()
      else: 
        print('invalid input')

  def play_new_hand(self):
    self.hand = Hand(self.hand_size)
    self.hand.deal_hand()
    self.hand.play_hand()

  def replay_hand(self):
    if self.hand != None:
      self.hand.play_hand()
    else: 
      print('You have not played a hand yet. Please play a new hand first!')

  def exit_game(self):
    return

game = Game(int(input('how many letters in a hand')))
game.play_game()


  