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
        return self.map_alphabet([string.ascii_lowercase, string.ascii_uppercase], shift)

    def map_alphabet(self, alphabets, shift):
        def mapped_letter(letter, alphabet):
          return alphabet[(alphabet.index(letter) + shift) - 26]
        return {letter: mapped_letter(letter, alphabet) for alphabet in alphabets for letter in alphabet}

    def apply_shift(self, shift):
        if 0 <= shift < 26:
            cipher_dict = self.build_shift_dict(shift)
            return ''.join([cipher_dict[char] 
                if char.isalpha() else char 
                for char in self.get_message_text()])
        #return ''.join([self.build_shift_dict(shift)[char] if char.isalpha() else char for char in self.get_message_text() if 0 <= shift < 26])