import random

#with truncating and starting at 50 each time for the class
def get_user_input(guess):
  print('Is your secret number ' + str(guess) + '?')
  return (input("Enter 'h' to indicate the guess is too high."
  + " Enter 'l' to indicate the guess is too low."
  + " Enter 'c' to indicate I guessed correctly.")) 

def guess_number_class():
  user_input = ''
  guess = 50
  high = 100
  low = 0

  print('Please think of a number between 0 and 100!')
  while user_input != 'c':
    user_input = get_user_input(guess)
    if user_input == 'h':
      high = guess
      guess = int(low + (high - low)/2)
    elif user_input == 'l': 
      low = guess
      guess = int(low + (high - low)/2)
    elif user_input == 'c':
      print('Game over. Your secret number was: ' + str(guess))
    elif user_input != 'l' or user_input != 'h' or user_input != 'c':
      print('Sorry, I did not understand your input.')
  
#with rounding instead of truncating and starts with random guess value instead of 50
def get_user_input_with_rounding(guess):
  print('Is your secret number ' + str(guess) + '?')
  return (input("Enter 'h' to indicate the guess is too high."
  + " Enter 'l' to indicate the guess is too low."
  + " Enter 'c' to indicate I guessed correctly.")) 

def guess_number():
  user_input = ''
  guess = random.randint(0, 100)
  high = 100
  low = 0

  print('Please think of a number between 0 and 100!')
  while user_input != 'c':
    user_input = get_user_input_with_rounding(guess)
    if user_input == 'h':
      high = guess
      guess = round(low + (high - low)/2)
    elif user_input == 'l': 
      low = guess
      guess = round(low + (high - low)/2)
    elif user_input == 'c':
      print('Game over. Your secret number was: ' + str(guess))
    elif user_input != 'l' or user_input != 'h' or user_input != 'c':
      print('Sorry, I did not understand your input.')
    
guess_number()
