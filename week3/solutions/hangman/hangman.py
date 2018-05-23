import os
import random
import string

current_dir = os.path.dirname(os.path.abspath(__file__))
WORDLIST_FILENAME = os.path.join(current_dir, 'words.txt')

def load_words():
  """
  Returns a list of valid words. Words are strings of lowercase letters.
    
  Depending on the size of the word list, this function may
  take a while to finish.
  """
  print("Loading word list from file...")
  in_file = open(WORDLIST_FILENAME, 'r')
  line = in_file.readline()
  wordlist = line.split()
  print("  ", len(wordlist), "words loaded.")
  return wordlist

def choose_word(wordlist):
  """
  wordlist (list): list of words (strings)

  Returns a word from wordlist at random
  """
  return random.choice(wordlist)

def is_word_guessed(secret_word, letters_guessed):
  '''
  secret_word: string, the word the user is guessing
  letters_guessed: list, what letters have been guessed so far
  returns: boolean, True if all the letters of secret_word are in letters_guessed;
  False otherwise
  '''
  is_word_guessed = False
  for letter in secret_word:
    if letter in letters_guessed:
      is_word_guessed = True
    else:
      return False
  return is_word_guessed

def get_guessed_word(secret_word, letters_guessed):
  '''
  secret_word: string, the word the user is guessing
  letters_guessed: list, what letters have been guessed so far
  returns: string, comprised of letters and underscores that represents
  what letters in secret_word have been guessed so far.
  '''
  guessed_letters = ''
  for letter in secret_word:
    if letter in letters_guessed:
      guessed_letters += letter
    else:
      guessed_letters += '_'
  return guessed_letters

def get_available_letters(letters_guessed):
  '''
  letters_guessed: list, what letters have been guessed so far
  returns: string, comprised of letters that represents what letters have not
  yet been guessed.
  '''
  alphabet = string.ascii_lowercase
  available_letters = ''
  for letter in alphabet:
    if letter not in letters_guessed:
      available_letters += letter
  return available_letters

def hangman(secret_word):
  '''
  secret_word: string, the secret word to guess.

  Starts up an interactive game of Hangman.

  * At the start of the game, let the user know how many 
    letters the secret_word contains.

  * Ask the user to supply one guess (i.e. letter) per round.

  * The user should receive feedback immediately after each guess 
    about whether their guess appears in the computers word.

  * After each round, you should also display to the user the 
    partially guessed word so far, as well as letters that the 
    user has not yet guessed.

  Follows the other limitations detailed in the problem write-up.
  '''
  is_playing = True
  guesses_left = 8
  letters_guessed = []

  greeting(secret_word)

  while is_playing:
    display_game_info(guesses_left, letters_guessed)
    guess = input('Please guess a letter: ').lower()
    
    if guess in letters_guessed:
      show_repeat_letter_message(secret_word, letters_guessed)
    else:
      letters_guessed.append(guess)
      if guess in secret_word:
        is_playing = process_successful_guess(letters_guessed, is_playing, secret_word)
      elif guess not in secret_word:
        guesses_left = process_failed_guess(guesses_left, letters_guessed, secret_word)

    is_playing = end_game(guesses_left, secret_word)

def greeting(secret_word):
  print('Welcome to the game, Hangman!')
  print('I am thinking of a word that is ' + str(len(secret_word)) + ' letters long.')

def display_game_info(guesses_left, letters_guessed):
  print('-----------')
  print('You have ' + str(guesses_left) + ' guesses left.')
  print('Available letters: ' +  get_available_letters(letters_guessed))

def end_game(guesses_left, secret_word):
  if guesses_left <= 0: 
    print('-----------')
    print('Sorry, you ran out of guesses. The word was ' + secret_word + '.')
    return False      
  return True

def process_successful_guess(letters_guessed, is_playing, secret_word):
  show_successful_letter_message(secret_word, letters_guessed)
  if is_word_guessed(secret_word, letters_guessed):
    is_playing = process_winning_game()
  return is_playing

def process_winning_game():
  print('-----------')
  print('Congratulations, you won!')
  return False

def process_failed_guess(guesses_left, letters_guessed, secret_word):
  guesses_left -= 1
  show_failed_letter_message(secret_word, letters_guessed)  
  return guesses_left

def show_successful_letter_message(secret_word, letters_guessed):
  print('Good guess: ' + get_guessed_word(secret_word, letters_guessed))

def show_failed_letter_message(secret_word, letters_guessed):
  print('Oops! That letter is not in my word: ' + get_guessed_word(secret_word, letters_guessed))

def show_repeat_letter_message(secret_word, letters_guessed):
  print('Oops! You\'ve already guessed that letter: ' + get_guessed_word(secret_word, letters_guessed))
