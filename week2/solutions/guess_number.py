import random

#with truncating
def get_user_input(guess):
  print('Is your secret number ' + str(guess) + '?')
  return (input("Enter 'h' to indicate the guess is too high."
  + " Enter 'l' to indicate the guess is too low."
  + " Enter 'c' to indicate I guessed correctly.")) 

userInput = ''
guess = 50 #random.randint(0, 100)
high = 100
low = 0

print('Please think of a number between 0 and 100!')
while userInput != 'c':
  userInput = getUserInput(guess)
  if userInput == 'h':
    high = guess
    guess = int(low + (high - low)/2)
  elif userInput == 'l': 
    low = guess
    guess = int(low + (high - low)/2)
  elif userInput == 'c':
    print('Game over. Your secret number was: ' + str(guess))
  elif userInput != 'l' or userInput != 'h' or userInput != 'c':
    print('Sorry, I did not understand your input.')
  
#with rounding instead of truncating
def get_user_input_with_rounding(guess):
  print('Is your secret number ' + str(guess) + '?')
  return (input("Enter 'h' to indicate the guess is too high."
  + " Enter 'l' to indicate the guess is too low."
  + " Enter 'c' to indicate I guessed correctly.")) 

userInput = ''
guess = random.randint(0, 100)
high = 100
low = 0

print('Please think of a number between 0 and 100!')
while userInput != 'c':
  userInput = getUserInput(guess)
  if userInput == 'h':
    high = guess
    guess = round(low + (high - low)/2)
  elif userInput == 'l': 
    low = guess
    guess = round(low + (high - low)/2)
  elif userInput == 'c':
    print('Game over. Your secret number was: ' + str(guess))
  elif userInput != 'l' or userInput != 'h' or userInput != 'c':
    print('Sorry, I did not understand your input.')
  
