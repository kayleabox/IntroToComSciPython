from hangman import load_words
from hangman import choose_word
from hangman import hangman

wordlist = load_words()
secret_word = choose_word(wordlist).lower()
hangman(secret_word)