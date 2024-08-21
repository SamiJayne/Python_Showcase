# WELCOME TO MY PYTHON SHOWCASE
# DAY 83 of the 100 DAYS OF PYTHON CODE BY ANGELA
# PROJECT 2 is TIC TAC TOE

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

players = input("How many players? 1 or 2? \n")

def winning_player(dictionary):
    if ((GAME_DICT[1] + GAME_DICT[2] + GAME_DICT[3] == 'OOO') or (GAME_DICT[1] + GAME_DICT[2] +GAME_DICT[3] == 'XXX') or
       (GAME_DICT[4] + GAME_DICT[5] + GAME_DICT[6] == 'OOO') or (GAME_DICT[4] + GAME_DICT[5] + GAME_DICT[6] == 'XXX') or
       (GAME_DICT[7] + GAME_DICT[8] + GAME_DICT[9] == 'OOO') or (GAME_DICT[7] + GAME_DICT[8] + GAME_DICT[9] == 'XXX') or
       (GAME_DICT[1] + GAME_DICT[4] + GAME_DICT[7] == 'OOO') or (GAME_DICT[1] + GAME_DICT[4] + GAME_DICT[7] == 'XXX') or
       (GAME_DICT[2] + GAME_DICT[5] + GAME_DICT[8] == 'OOO') or (GAME_DICT[2] + GAME_DICT[5] + GAME_DICT[8] == 'XXX') or
       (GAME_DICT[3] + GAME_DICT[6] + GAME_DICT[9] == 'OOO') or (GAME_DICT[3] + GAME_DICT[6] + GAME_DICT[9] == 'XXX') or
       (GAME_DICT[1] + GAME_DICT[5] + GAME_DICT[9] == 'OOO') or (GAME_DICT[1] + GAME_DICT[5] + GAME_DICT[9] == 'XXX') or
       (GAME_DICT[3] + GAME_DICT[5] + GAME_DICT[7] == 'OOO') or (GAME_DICT[3] + GAME_DICT[5] + GAME_DICT[7] == 'XXX')):
       print("Winner!")
       game_is_on = False
       # Find a way to return the winner :)
    else:
        return


def update_game_board(dictionary):
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
        pass
    else:
        print("You cannot play a move there, please try again:")
        player_move(player, dictionary)
        # need to have move -1 here! global / local variables


def player_move(player, dictionary):
    if player == 1:
        symbol = 'O'
    else:
        symbol = 'X'
    game_move = int(input("Enter a number between 1 and 9:\n"))
    check_position_is_free(player, game_move, GAME_DICT)
    GAME_DICT.update({game_move: symbol})
    update_game_board(GAME_DICT)
    winning_player(GAME_DICT)


game_is_on = True

if int(players) == 2:
    print(welcome)
    print(GAME_BOARD_POSITIONS)
    print("Player 1 you are 'O' Player 2 you are 'X' \nPlayer 1 your turn: ")
    print(GAME_BOARD)
    move = 1

    while game_is_on:
        if move in (1, 3, 5, 7, 9):
            player_move(1, GAME_DICT)
            move += 1
        if move in (2, 4, 6, 8):
            player_move(2, GAME_DICT)
            move += 1
    else:
        print("GAME OVER")
