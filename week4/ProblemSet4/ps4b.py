from ps4a import *
import time


#
#
# Computer chooses a word
#
#
def compChooseWord(hand, wordList, n):
    """
    Given a hand and a wordList, find the word that gives 
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)

    returns: string or None
    """
    # Create a new variable to store the maximum score seen so far (initially 0)
    bestScore = 0
    # Create a new variable to store the best word seen so far (initially None)  
    bestWord = None
    # For each word in the wordList
    for word in wordList:
        # If you can construct the word from your hand
        if isValidWord(word, hand, wordList):
            # find out how much making that word is worth
            score = getWordScore(word, n)
            # If the score for that word is higher than your best score
            if (score > bestScore):
                # update your best score, and best word accordingly
                bestScore = score
                bestWord = word
    # return the best word you found.
    return bestWord

#
# Computer plays a hand
#
def compPlayHand(hand, wordList, n):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer 
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is 
    displayed, the remaining letters in the hand are displayed, and the 
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).
 
    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    """
    # Keep track of the total score
    totalScore = 0
    # As long as there are still letters left in the hand:
    while (calculateHandlen(hand) > 0) :
        # Display the hand
        print("Current Hand: ", end=' ')
        displayHand(hand)
        # computer's word
        word = compChooseWord(hand, wordList, n)
        # If the input is a single period:
        if word == None:
            # End the game (break out of the loop)
            break
            
        # Otherwise (the input is not a single period):
        else :
            # If the word is not valid:
            if (not isValidWord(word, hand, wordList)) :
                print('This is a terrible error! I need to check my own code!')
                break
            # Otherwise (the word is valid):
            else :
                # Tell the user how many points the word earned, and the updated total score 
                score = getWordScore(word, n)
                totalScore += score
                print('"' + word + '" earned ' + str(score) + ' points. Total: ' + str(totalScore) + ' points')              
                # Update hand and show the updated hand to the user
                hand = updateHand(hand, word)
                print()
    # Game is over (user entered a '.' or ran out of letters), so tell user the total score
    print('Total score: ' + str(totalScore) + ' points.')

def computer_play_hand(hand, wordList, HAND_SIZE):
    total_score = 0
    while sum(hand.values()) > 0: 
        displayHand(hand)
        computer_word = get_computer_word(hand, wordList, HAND_SIZE)
        if computer_word == '':
            break
        else:
            if not isValidWord(computer_word, hand, wordList):
                print('invalid word \n')
            else:
                score = getWordScore(computer_word, HAND_SIZE)
                total_score += score
                print('" ' + computer_word + ' " earned ' + str(score) + ' points for that word! Your new score is ' + str(total_score)) 
                hand = updateHand(hand, computer_word)

    # Game is over (user entered a '.' or ran out of letters), so tell user the total score
    print('Ran out of letters. Total: ' + str(total_score))

def get_computer_word(hand, wordList, n):
    computer_word = ''
    high_score = 0
    for word in wordList: 
        if isValidWord(word, hand, wordList):
            score = getWordScore(word, n)
            if score > high_score: 
                computer_word = word
                high_score = score
    return computer_word


#
# Problem #6: Playing a game
#
#
def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
      
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """
    hand = {}
    game_type = 'n'
    player_type = ''

    while game_type != 'e':
        game_type = input('for a new game enter "n", to replay the last game enter "r"' + 
        ' and to exit enter "e": ')

        if game_type == 'e':
            return
        elif game_type == 'r' and hand == {}: 
            print('You have not played a hand yet. Please play a new hand first!')
        elif game_type == 'n' or game_type == 'r':
            player_type = get_player_type()
            player_type, hand = prepare_game_settings(player_type, game_type, hand)
        else: 
            print('invalid input')
   
def get_player_type():
    player_type = ''
    while player_type != 'c' and player_type != 'u':
        player_type = input('Enter u to have yourself play, c to have the computer play: ')
        if player_type != 'c' and player_type != 'u':
            print('invalid command')
    return player_type
    
def prepare_game_settings(player_type, game_type, hand):
    play_game_as = {
        'c': compPlayHand,
        'u': playHand
    }

    if player_type != '':
        if game_type == 'n' or game_type == 'r':
            if game_type == 'n':
                hand = dealHand(HAND_SIZE)
            return play_game_as[player_type](hand, wordList, HAND_SIZE), hand

#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordList = loadWords()
    computer_play_hand({'a': 2, 'm': 1}, wordList, 3)
    computer_play_hand({'a': 2, 'm': 1, 't': 1, 'u': 1, 'r': 1, 'e': 1}, wordList, 7)
    computer_play_hand({'a': 1, 'i': 1, 'y': 1, 'k': 1, 's': 1, 'x': 2}, wordList, 7)
    #"axis" score 44
    computer_play_hand({'o': 1, 'a': 1, 'g': 1, 'q': 1, 'b': 1, 'w': 1, 'j': 1}, wordList, 7)
    #"jaw" score 39, "bog" score 18 total 57
    playGame(wordList)


