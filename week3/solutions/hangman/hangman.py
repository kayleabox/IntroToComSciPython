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
      guessed_letters += ' _ '
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
  print('Welcome to the game, Hangman!')
  print('I am thinking of a word that is ' + str(len(secret_word)) + ' letters long.')
  is_playing = True
  guesses_left = 8
  letters_guessed = []

  while is_playing:
    print('-----------')
    print('You have ' + str(guesses_left) + ' guesses left.')
    print('Available letters: ' +  get_available_letters(letters_guessed))
    guess = input('Please guess a letter: ').lower()
    if guess in secret_word and guess not in letters_guessed:
      letters_guessed.append(guess)
      print('Good guess: ' + get_guessed_word(secret_word, letters_guessed))
      if is_word_guessed(secret_word, letters_guessed):
        print('-----------')
        print('Congratulations, you won!')
        is_playing = False
    elif guess in letters_guessed:
      print('Oops! You\'ve already guessed that letter: ' + get_guessed_word(secret_word, letters_guessed))
    else:
      guesses_left -= 1
      letters_guessed.append(guess)
      print('Oops! That letter is not in my word: ' + get_guessed_word(secret_word, letters_guessed))

    if guesses_left <= 0: 
      print('-----------')
      print('Sorry, you ran out of guesses. The word was ' + secret_word + '.')
      is_playing = False      

wordlist = load_words()
secret_word = choose_word(wordlist).lower()
hangman(secret_word)
