from cipher_text_message import CipherTextMessage
from decrypt_story import decrypt_story
from message import Message
from plain_text_message import PlainTextMessage

message = Message('hello')
print(message.build_shift_dict(6))
print(message.apply_shift(2))

#Example test case (CiphertextMessage)
ciphertext = CipherTextMessage('jgnnq')
print('Expected Output:', (24, 'hello'))
print('Actual Output:', ciphertext.decrypt_message())
ciphertext = CipherTextMessage('Lmlqclqc umpbq: uypk ilmujcbec bcqi npmmd sqsyj')
print(ciphertext.decrypt_message())
print(decrypt_story())

#Example test case (PlaintextMessage)
plaintext = PlainTextMessage('hello', 2)
print('Expected Output: jgnnq')
print('Actual Output:', plaintext.get_message_text_encrypted())