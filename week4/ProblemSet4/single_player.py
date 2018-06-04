import os
import random
import string

from load_words import load_words
#When running tests I have to add ProblemSet4 dir to the path or esle it errors
#Need to figure out why
#from ProblemSet4.load_words import load_words

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

def get_word_score(word, n):
    """
    Returns the score for a word. Assumes the word is a valid word.

    The score for a word is the sum of the points for letters in the
    word, multiplied by the length of the word, PLUS 50 points if all n
    letters are used on the first turn.

    Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is
    worth 3, D is worth 2, E is worth 1, and so on (see SCRABBLE_LETTER_VALUES)

    word: string (lowercase letters)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    returns: int >= 0
    """
    score = 0
    for letter in word:
        score = score + SCRABBLE_LETTER_VALUES[letter]
    score *= len(word)
    if len(word) == n: 
        score += 50
    return score

def display_hand(hand):
    """
    Displays the letters currently in the hand.

    hand: dictionary (string -> int)
    """
    for letter in hand.keys():
        for j in range(hand[letter]):
             print(letter,end=" ")
    print()

def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    At least n/3 the letters in the hand should be VOWELS.

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    hand={}
    num_vowels = n // 3
    
    for i in range(num_vowels):
        vowel = VOWELS[random.randrange(0,len(VOWELS))]
        hand[vowel] = hand.get(vowel, 0) + 1
        
    for i in range(num_vowels, n):    
        consonant = CONSONANTS[random.randrange(0,len(CONSONANTS))]
        hand[consonant] = hand.get(consonant, 0) + 1
        
    return hand

def update_hand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    updated_hand = hand.copy()
    for letter in word:
        updated_hand[letter] -= 1
    return updated_hand

def is_valid_word(word, hand, word_list):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or word_list.
   
    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    """
    if word == '': 
        return False
    letters_in_word = create_letter_dict(word)
    for key in letters_in_word:
        if key not in hand or hand[key] < letters_in_word[key]: 
            return False
    return word in word_list

def create_letter_dict(word):
    letters_in_word = {}
    for letter in word:
        if letter not in letters_in_word: 
            letters_in_word[letter] = 1
        else: 
            letters_in_word[letter] += 1
    return letters_in_word

def calculate_hand_len(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: integer
    """
    number_in_hand = 0
    for key in hand: 
        number_in_hand += hand[key]
    return number_in_hand


def play_hand(hand, word_list, n):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    * The user may input a word or a single period (the string ".") 
      to indicate they're done playing
    * Invalid words are rejected, and a message is displayed asking
      the user to choose another word until they enter a valid word or "."
    * When a valid word is entered, it uses up letters from the hand.
    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.
    * The sum of the word scores is displayed when the hand finishes.
    * The hand finishes when there are no more unused letters or the user
      inputs a "."

      hand: dictionary (string -> int)
      word_list: list of lowercase strings
      n: integer (HAND_SIZE; i.e., hand size required for additional points)
      
    """
    total_score = 0
    while sum(hand.values()) > 0: 
        display_hand(hand)
        user_word = input('Please enter a word or "." to indicate that you are finished: ')
        if user_word == '.':
            break     
        else:
            if not is_valid_word(user_word, hand, word_list):
                print('invalid word \n')
            else:
                hand, total_score = calculate_round(user_word, hand, total_score, n)
                
    if sum(hand.values()) <= 0:
        print('Ran out of letters!')
    print('Total: ' + str(total_score))

def calculate_round(word, hand, total_score, n):
    score = get_word_score(word, n)
    total_score += score
    print('" ' + word + ' " earned ' + str(score) + ' points for that word! Your new score is ' + str(total_score))
    return update_hand(hand, word), total_score

def play_game(word_list):
    """
    Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
      * If the user inputs 'n', let the user play a new (random) hand.
      * If the user inputs 'r', let the user play the last hand again.
      * If the user inputs 'e', exit the game.
      * If the user inputs anything else, tell them their input was invalid.

    2) When done playing the hand, repeat from step 1    
    """
    hand = {}
    playing = 'n'
    while playing != 'e':
        playing = input('for a new game enter "n", to replay the last game enter "r"' + 
        ' and to exit enter "e"')
        if playing == 'n':
            hand = deal_hand(HAND_SIZE)
            play_hand(hand, word_list, HAND_SIZE)
        elif playing == 'r':
            if hand != {}:
                play_hand(hand, word_list, HAND_SIZE)
            else: 
                print('You have not played a hand yet. Please play a new hand first!')
        elif playing == 'e':
            return
        else: 
            print('invalid input')
         
if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)