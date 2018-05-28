import os
import string

from Message import Message

current_dir = os.path.dirname(os.path.abspath(__file__))
STORY_FILE = os.path.join(current_dir, 'story.txt')

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
        real_words = 0 
        return [real_words + 1 for word in new_words if self.is_word(self.get_valid_words(), word)]

    def is_word(self, word_list, word):
        word = word.lower()
        word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
        return word in word_list

def get_story_string():
    f = open(STORY_FILE, "r")
    story = str(f.read())
    f.close()
    return story

def decrypt_story():
    ciphertext = CiphertextMessage(get_story_string())
    return ciphertext.decrypt_message()

'''
#Example test case (CiphertextMessage)
ciphertext = CipherTextMessage('jgnnq')
print('Expected Output:', (24, 'hello'))
print('Actual Output:', ciphertext.decrypt_message())
ciphertext = CipherTextMessage('Lmlqclqc umpbq: uypk ilmujcbec bcqi npmmd sqsyj')
print(ciphertext.decrypt_message())'''