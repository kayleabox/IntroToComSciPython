import os
import string

current_dir = os.path.dirname(os.path.abspath(__file__))
WORDLIST_FILENAME = os.path.join(current_dir, 'words.txt')

def load_words(file_name):
    in_file = open(file_name, 'r')
    line = in_file.readline()
    word_list = line.split()
    in_file.close()
    return word_list

class Message(object):
    def __init__(self, text):
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)

    def get_message_text(self):
        return self.message_text

    def get_valid_words(self):
        return self.valid_words[:]
        
    def build_shift_dict(self, shift):
        alphabet = string.ascii_lowercase
        return dict(list(self.map_alphabet(alphabet, shift).items()) 
        + list(self.map_alphabet(alphabet.upper(), shift).items()))

    def map_alphabet(self, alphabet, shift):
        return {l: alphabet[(alphabet.index(l) + shift) - 26] for l in alphabet}

    def apply_shift(self, shift):
        if 0 <= shift < 26:
            cipher_dict = self.build_shift_dict(shift)
            return ''.join([cipher_dict[letter] if letter.isalpha() else letter for letter in self.message_text])

'''
message = Message('hello')
print(message.build_shift_dict(6))
print(message.apply_shift(2))'''