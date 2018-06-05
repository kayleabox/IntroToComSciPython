import os
import string

from message import Message

class CipherTextMessage(Message):
    def __init__(self, text):
        Message.__init__(self, text)

    def decrypt_message(self):
        decrypted_text = self.get_decrypted_text_array()
        real_words = self.create_real_words_dict(decrypted_text)
        shift = max(real_words, key=real_words.get)
        return (shift,  decrypted_text[shift])

    def get_decrypted_text_array(self):
        return [self.apply_shift(n) for n in range(0, 25)]

    def create_real_words_dict(self, decrypted_text):
        return {decrypted_text.index(element) : self.count_real_words(element.split(' ')) for element in decrypted_text}

    def count_real_words(self, new_words):
        return len([word for word in new_words if self.is_word(self.get_valid_words(), word)])

    def is_word(self, word_list, word):
        return word.lower().strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"") in word_list
