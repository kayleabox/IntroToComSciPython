import os
import sys
import unittest
import unittest.mock

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))

from score import Score
from word import Word

#Score.get_total()
#Score.get_round()
#Score.set_total()
#Score.set_round()
#Score.reset()
class ScoreTest2(unittest.TestCase):
  def test(self):
    score = Score()
    
    self.assertEqual(score.get_total(), 0)
    self.assertEqual(score.get_round(), 0)
    self.assertEqual(score.set_total(4), None)
    self.assertEqual(score.get_total(), 4)
    self.assertEqual(score.set_round(15), None)
    self.assertEqual(score.get_round(), 15)
    self.assertEqual(score.set_total(-5), None)
    self.assertEqual(score.get_total(), -5)
    self.assertEqual(score.set_round(-1), None)
    self.assertEqual(score.get_round(), -1)
    self.assertEqual(score.reset(), None)
    self.assertEqual(score.get_total(), 0)
    self.assertEqual(score.get_round(), 0)


#Score.calculate()
score = Score()
class ScoreCalculateTest(unittest.TestCase):
  @unittest.mock.patch('score.Score.display')
  def mock_display_function(self, mock_display_score):
    score.calculate(Word('zebra'), 7)

    self.assertTrue(mock_display_score.called)  

  def test(self):
    self.mock_display_function()
    self.assertEqual(score.get_round(), 80)
    self.assertEqual(score.get_total(), 80)

class ScoreCalculateTest2(unittest.TestCase):
  @unittest.mock.patch('score.Score.display')
  def mock_display_function(self, mock_display_score):
    score.calculate(Word('zebra'), 5)

    self.assertTrue(mock_display_score.called)  

  def test(self):
    self.mock_display_function()
    self.assertEqual(score.get_round(), 130)
    self.assertEqual(score.get_total(), 210)


#Score.display()
class ScoreDisaplyTest1(unittest.TestCase):
  @unittest.mock.patch('score.Score.get_total')
  @unittest.mock.patch('score.Score.get_round')
  def mock_get_function(self, mock_get_total, mock_get_round):
    score.display(Word('zebra'))

    self.assertTrue(mock_get_total.called) 
    self.assertTrue(mock_get_round.called)  

  def test(self):
    self.mock_get_function()
    self.assertEqual(score.get_round(), 130)
    self.assertEqual(score.get_total(), 210)