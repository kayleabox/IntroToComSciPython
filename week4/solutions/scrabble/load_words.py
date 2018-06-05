import os
import string

current_dir = os.path.dirname(os.path.abspath(__file__))
WORDLIST_FILENAME = os.path.join(current_dir, 'words.txt')

def load_words():
    with open(WORDLIST_FILENAME, 'r') as in_file:
        return [ line.strip().lower() for line in in_file ]

