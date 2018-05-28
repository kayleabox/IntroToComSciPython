import os
import sys
import unittest
import unittest.mock

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))

from Game import Game

class GameGetTest1(unittest.TestCase):
  def test(self):
    self.assertEqual(Game().get_status(), 'n')

class GameGetTest2(unittest.TestCase):
  def test(self):
    game = Game()
    game.status = 'e'
    self.assertEqual(game.get_status(), 'e')

class GameGetStatusDictTest1(unittest.TestCase):
  def test(self):
    game = Game()
    self.assertEqual(game.get_status_dict(), game.status_dict)
    self.assertEqual(game.get_status_dict() is game.status_dict, False)
    self.assertIsInstance(game.get_status_dict(), dict)



#Game.start()
class GameStartTest1(unittest.TestCase):
  @unittest.mock.patch('Game.Game.set_status')
  @unittest.mock.patch('Game.Game.get_status')
  @unittest.mock.patch('Game.Game.play')  
  def mock_game_start_function(self, mock_set_status, mock_get_status, mock_play):
    game = Game()
    mock_get_status.side_effect = ['n', 'e']
    game.start()

    self.assertTrue(mock_set_status.called)
    self.assertTrue(mock_get_status.called)
    self.assertTrue(mock_play.called)

  def test(self):
    self.mock_game_start_function()

class GameStartTest2(unittest.TestCase):
  @unittest.mock.patch('Game.Game.set_status')
  @unittest.mock.patch('Game.Game.get_status')
  @unittest.mock.patch('Game.Game.play')  
  def mock_game_start_function(self, mock_set_status, mock_get_status, mock_play):
    game = Game()
    mock_get_status.side_effect = ['r', 'e']
    game.start()

    self.assertTrue(mock_set_status.called)
    self.assertTrue(mock_get_status.called)
    self.assertTrue(mock_play.called)

  def test(self):
    self.mock_game_start_function()

#Game.play()
class GamePlayTest1(unittest.TestCase):
  @unittest.mock.patch('Game.Game.play_new_hand')  
  def mock_game_play_function(self, mock_play_new_hand):
    game = Game()
    game.play()

    self.assertTrue(mock_play_new_hand.called)

  def test(self):
    self.mock_game_play_function()

class GamePlayTest2(unittest.TestCase):
  @unittest.mock.patch('Game.Game.replay_hand')  
  def mock_game_play_function(self, mock_replay_hand):
    game = Game()
    game.status = 'r'
    game.play()

    self.assertTrue(mock_replay_hand.called)

  def test(self):
    self.mock_game_play_function()
    
#Game.play_new_hand()


#Game.replay_hand()


#Game.exit()


#Game.set_hand_size