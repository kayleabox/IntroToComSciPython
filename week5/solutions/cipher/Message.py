import string

from load_words import load_words

class Message(object):
    def __init__(self, text):
        self.message_text = text
        self.valid_words = load_words()

    def get_message_text(self):
        return self.message_text

    def get_valid_words(self):
        return self.valid_words[:]
        
    def build_shift_dict(self, shift):
        alphabet = string.ascii_lowercase
        return dict(list(self.map_alphabet(alphabet, shift).items()) 
        + list(self.map_alphabet(alphabet.upper(), shift).items()))

    def map_alphabet(self, alphabet, shift):
        return {letter: alphabet[(alphabet.index(letter) + shift) - 26] for letter in alphabet}

    def apply_shift(self, shift):
        if 0 <= shift < 26:
            cipher_dict = self.build_shift_dict(shift)
            return ''.join([cipher_dict[char] if char.isalpha() else char for char in self.get_message_text()])
        #return ''.join([self.build_shift_dict(shift)[char] if char.isalpha() else char for char in self.get_message_text() if 0 <= shift < 26])