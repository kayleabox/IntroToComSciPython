import os

from CipherTextMessage import CipherTextMessage

current_dir = os.path.dirname(os.path.abspath(__file__))
STORY_FILE = os.path.join(current_dir, 'story.txt')

def get_story_string():
    with open(STORY_FILE, "r") as story_file:
        return str(story_file.read())

def decrypt_story():
    ciphertext = CipherTextMessage(get_story_string())
    return ciphertext.decrypt_message()
    #return CipherTextMessage(get_story_string()).decrypt_message()