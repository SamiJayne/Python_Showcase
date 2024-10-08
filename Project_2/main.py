# WELCOME TO MY PYTHON SHOWCASE
# DAY 83 of the 100 DAYS OF PYTHON CODE BY ANGELA
# PROJECT 2 is TIC TAC TOE

import random

GAME_BOARD_POSITIONS = (" 1 | 2 | 3 \n"
                        "-----------\n"
                        " 4 | 5 | 6 \n"
                        "-----------\n"
                        " 7 | 8 | 9 \n")

GAME_BOARD = ("   |   |   \n"
              "-----------\n"
              "   |   |   \n"
              "-----------\n"
              "   |   |   \n")

GAME_DICT = {
    1: " ",
    2: " ",
    3: " ",
    4: " ",
    5: " ",
    6: " ",
    7: " ",
    8: " ",
    9: " "}

welcome = "WELCOME TO TIC TAC TOE HERE ARE YOUR GAME POSITIONS:\n"

global move


def check_for_draw(dictionary):
    count = 0
    global game_is_on
    for item in dictionary.values():
        if item == ' ':
            count += 1
    if count == 0:
        game_is_on = False
        print("No Winner, it's a draw!")
        return True
    else:
        return False


def winning_player(dictionary):
    if ((GAME_DICT[1] + GAME_DICT[2] + GAME_DICT[3] == 'OOO') or
            (GAME_DICT[4] + GAME_DICT[5] + GAME_DICT[6] == 'OOO') or
            (GAME_DICT[7] + GAME_DICT[8] + GAME_DICT[9] == 'OOO') or
            (GAME_DICT[1] + GAME_DICT[4] + GAME_DICT[7] == 'OOO') or
            (GAME_DICT[2] + GAME_DICT[5] + GAME_DICT[8] == 'OOO') or
            (GAME_DICT[3] + GAME_DICT[6] + GAME_DICT[9] == 'OOO') or
            (GAME_DICT[1] + GAME_DICT[5] + GAME_DICT[9] == 'OOO') or
            (GAME_DICT[3] + GAME_DICT[5] + GAME_DICT[7] == 'OOO')):
        print("Winner is O!")
        global game_is_on
        game_is_on = False
    elif ((GAME_DICT[1] + GAME_DICT[2] + GAME_DICT[3] == 'XXX') or
          (GAME_DICT[4] + GAME_DICT[5] + GAME_DICT[6] == 'XXX') or
          (GAME_DICT[7] + GAME_DICT[8] + GAME_DICT[9] == 'XXX') or
          (GAME_DICT[1] + GAME_DICT[4] + GAME_DICT[7] == 'XXX') or
          (GAME_DICT[2] + GAME_DICT[5] + GAME_DICT[8] == 'XXX') or
          (GAME_DICT[3] + GAME_DICT[6] + GAME_DICT[9] == 'XXX') or
          (GAME_DICT[1] + GAME_DICT[5] + GAME_DICT[9] == 'XXX') or
          (GAME_DICT[3] + GAME_DICT[5] + GAME_DICT[7] == 'XXX')):
        print("Winner is X!")
        game_is_on = False
    else:
        check_for_draw(GAME_DICT)
        return


def update_game_board(dictionary):
    # clear the screen
    GAME_BOARD_POSITIONS = (" 1 | 2 | 3 \n"
                            "-----------\n"
                            " 4 | 5 | 6 \n"
                            "-----------\n"
                            " 7 | 8 | 9 \n")
    for move in GAME_DICT:
        GAME_BOARD_POSITIONS = GAME_BOARD_POSITIONS.replace(str(move), GAME_DICT[move])
    print(GAME_BOARD_POSITIONS)


def check_position_is_free(player, position, dictionary):
    if GAME_DICT[position] == ' ':
        return True
    else:
        print("You cannot play a move there, please try again")
        return False


def player_move(player, dictionary):
    if player == 1:
        symbol = 'O'
        game_move = int(input("Enter a number between 1 and 9:\n"))
    elif player == 2:
        symbol = 'X'
        game_move = int(input("Enter a number between 1 and 9:\n"))
    elif player == 3:
        symbol = 'X'
        game_move = random.randint(1, 9)

    global move
    if check_position_is_free(player, game_move, GAME_DICT):
        GAME_DICT.update({game_move: symbol})
        update_game_board(GAME_DICT)
        winning_player(GAME_DICT)
        move += 1
    else:
        player_move(player, dictionary)


# Set game mode, so we can stop when this is no longer true
game_is_on = True

# Find out how many players we have, if only 1 player, they will play the computer
players = input("How many players? 1 or 2? (If there is only 1 player it will be against the computer)\n")

print(welcome)
print(GAME_BOARD_POSITIONS)
if int(players) == 2:
    print("Player 1 you are 'O' the computer will play Player 2 as 'X' \nPlayer 1 your turn: ")
else:
    print("Player 1 you are 'O' Player 2 you are 'X' \nPlayer 1 your turn: ")
print(GAME_BOARD)
move = 1

while game_is_on:
    if move in (1, 3, 5, 7, 9) and game_is_on:
        player_move(1, GAME_DICT)

    if move in (2, 4, 6, 8) and game_is_on:
        if int(players) == 1:
            player_move(3, GAME_DICT)
        elif int(players) == 2:
            player_move(2, GAME_DICT)

else:
    print("GAME OVER")
