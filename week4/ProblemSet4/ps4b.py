import time 

from load_words import load_words
from ps4a import *

def play_computer_hand(hand, word_list, HAND_SIZE):
    total_score = 0
    while sum(hand.values()) > 0: 
        display_hand(hand)
        computer_word = get_computer_word(hand, word_list, HAND_SIZE)
        if computer_word == '':
            break
        else:
            if not is_valid_word(computer_word, hand, word_list):
                print('invalid word \n')
            else:
                score = get_word_score(computer_word, HAND_SIZE)
                total_score += score
                print('" ' + computer_word + ' " earned ' + str(score) + ' points for that word! Your new score is ' + str(total_score)) 
                hand = update_hand(hand, computer_word)

    print('Ran out of letters. Total: ' + str(total_score))

def get_computer_word(hand, word_list, n):
    computer_word = ''
    high_score = 0
    for word in word_list: 
        if is_valid_word(word, hand, word_list):
            score = get_word_score(word, n)
            if score > high_score: 
                computer_word = word
                high_score = score
    return computer_word


def play_game(word_list):
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
        'c': play_computer_hand,
        'u': play_hand
    }

    if player_type != '':
        if game_type == 'n' or game_type == 'r':
            if game_type == 'n':
                hand = deal_hand(HAND_SIZE)
            return play_game_as[player_type](hand, word_list, HAND_SIZE), hand


if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)


