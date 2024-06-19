"""EX01 - Simple Battleship - A cute step toward Battleship."""

__author__ = "730631751"

# prompting player 1
player_1_input_str: str = input("Pick a secret boat location between 1 and 4:")
player_1_input: int = int(player_1_input_str)
if player_1_input < 1:
    print("Error! " + player_1_input_str + " too low!")
    exit()
if player_1_input > 4:
    print("Error! " + player_1_input_str + " too high!")
    exit()

# prompting player 2
player_2_input_str: str = input("Guess a number between 1 and 4:")
player_2_input: int = int(player_2_input_str)
if player_2_input < 1:
    print("Error! " + player_2_input_str + " too low!")
    exit()
if player_2_input > 4:
    print("Error! " + player_2_input_str + " too high!")
    exit()

# printing a string of boxes
BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"

# making an emoji string
if player_2_input == 1:
    if player_1_input == player_2_input:
        print(RED_BOX + BLUE_BOX + BLUE_BOX + BLUE_BOX)
    else:
        print(WHITE_BOX + BLUE_BOX + BLUE_BOX + BLUE_BOX)
if player_2_input == 2:
    if player_1_input == player_2_input:
        print(BLUE_BOX + RED_BOX + BLUE_BOX + BLUE_BOX)
    else:
        print(BLUE_BOX + WHITE_BOX + BLUE_BOX + BLUE_BOX)
if player_2_input == 3:
    if player_1_input == player_2_input:
        print(BLUE_BOX + BLUE_BOX + RED_BOX + BLUE_BOX)
    else:
        print(BLUE_BOX + BLUE_BOX + WHITE_BOX + BLUE_BOX)
if player_2_input == 4:
    if player_1_input == player_2_input:
        print(BLUE_BOX + BLUE_BOX + BLUE_BOX + RED_BOX)
    else:
        print(BLUE_BOX + BLUE_BOX + BLUE_BOX + WHITE_BOX)

# checking user input for a match
if player_2_input == player_1_input:
    print("Correct! You hit the ship.")
if player_2_input != player_1_input:
    print("Incorrect! You missed the ship.")
