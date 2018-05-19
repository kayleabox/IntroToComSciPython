# The 6.00 Word Game
import os
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
    word_list = []
    for line in in_file:
        word_list.append(line.strip().lower())
    print("  ", len(word_list), "words loaded.")
    return word_list