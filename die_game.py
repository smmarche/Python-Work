#This program is a program to play a Die game.

import random


#Rolling the dice
def roll_die():
    """ Simulate a die roll """
    return random.randint(1, 6)


def player_turn(player_name, player_score):
    """
        Implements what happens on player's turn.
        Returns player's score, which represents+
        the player's total score.
    """
#this option lets the user roll hence r or pass
    option = 'r'
    while option == 'r':
        print(f'\n*******{player_name}\'s turn********\n')
#roll 3 times
        roll_1 = roll_die()
        roll_2 = roll_die()
        roll_3 = roll_die()
        print(f"Scores: {roll_1}, {roll_2}, and {roll_3}.")
#sum up all 3 rolls to the score
        player_score += roll_1+roll_3+roll_2
#if any roll is a 2 reset the score to 0
        if roll_1 == 2 or roll_2 == 2 or roll_3 == 2:
            player_score = 0
            print(f"{player_name} got at least one 2.")
            print(f"{player_name}'s score: {player_score}")
            print()
            print("Press <enter> to continue ...", end="")
            input("")
#move to the next player after the player gets a 2
            break
#if the player's score is over 18 print the score and move to the next player
        elif player_score > 18:
            print(f"{player_name}'s score: {player_score}")
            print()
            break
#if the dice isn't a 2 or the score isn't over 18 then give the player the
#option to pass or roll
        else:
            print(f"{player_name}'s score: {player_score}")
            print()
            option = input("(p)ass or (r)oll? ")
    return player_score


def main():
    """
        The main driver of the program. Call
        the player_turn() functions here.
    """
    player_name = input("Enter the first player name: ").title()
    other_player = input("Enter the second player name: ").title()
    player_name_score = 0
    other_player_score = 0

    while True:
#if both player scores are less than 18 then the game will keep going if not
#skip to the first if clause below
#so in the case that some rolls a 2, as long as both scores are below 18
#this will keep the game in play prompting the next person
        if player_name_score <= 18 and other_player_score <= 18:
            player_name_score = player_turn(player_name, player_name_score)
            other_player_score = player_turn(other_player, other_player_score)
        else:
            break
#if elif clauses for different winners and a draw scenario
    if player_name_score > other_player_score:
        print(f'{player_name} wins with a score of {player_name_score}')
    elif other_player_score > player_name_score:
        print(f'{other_player} wins with a score of {other_player_score}')
    elif player_name_score == other_player_score:
        print("Both players got the same score")
        print(f"{player_name}: {player_name_score}scores")
        print(f"{other_player}: {other_player_score}scores")

#makes the whole thing run


main()