"""Functional Battleship!"""

__author__ = "730631751"

from random import randint


# part 1: declaring input_guess
def input_guess(grid_size: int, entry: str) -> int:
    """Prompts and return a user's guess."""
    assert entry == "row" or entry == "column"
    guess: str = ""
    if entry == "row":
        guess = input("Guess a row: ")
    else:
        guess = input("Guess a column: ")
    guess_int: int = int(guess)
    while guess_int < 1 or guess_int > grid_size:
        new_entry: str = input(
            f"The grid is only {grid_size} by {grid_size}. Try again: "
        )
        guess_int = int(new_entry)
    return guess_int


# part 2: declaring print_grid
def print_grid(
    grid_size: int, row_input: int, column_input: int, guess_correct: bool
) -> None:
    """Printing a grid."""
    row_counter: int = 1
    BLUE_BOX: str = "\U0001F7E6"
    RED_BOX: str = "\U0001F7E5"
    WHITE_BOX: str = "\U00002B1C"
    result_box: str = ""
    if guess_correct is True:
        result_box = RED_BOX
    else:
        result_box = WHITE_BOX
    while row_counter <= grid_size:
        column_counter: int = 1
        row_1: str = ""
        while column_counter <= grid_size:
            if row_counter == row_input and column_counter == column_input:
                row_1 += result_box
            else:
                row_1 += BLUE_BOX
            column_counter += 1
        print(row_1)
        row_counter += 1


# part 3: declaring correct_guess
def correct_guess(
    secret_row: int, secret_column: int, row_input: int, column_input: int
) -> bool:
    """Tells user if they are correct."""
    if row_input == secret_row and column_input == secret_column:
        return True
    else:
        return False


# part 4: implementing main
def main(grid_size: int, secret_row: int, secret_column: int) -> None:
    """Tying it all together."""
    turn: int = 1
    correct_guesses: int = 0
    while turn <= 5 and correct_guesses < 1:
        print(f"===Turn {turn}/5===")
        row_input: int = int(input_guess(grid_size, "row"))
        column_input: int = int(input_guess(grid_size, "column"))
        correct: bool = correct_guess(
            secret_row, secret_column, row_input, column_input
        )
        print_grid(grid_size, row_input, column_input, correct)
        if correct_guess(secret_row, secret_column, row_input, column_input) is True:
            print(f"Hit! You won in {turn}/5 turns!")
            correct_guesses += 1
        else:
            print("Miss!")
            turn += 1
    if turn > 5 and correct_guesses < 1:
        print("X/5 - Better luck next time!")


# icing on the cake
if __name__ == "__main__":
    grid_size: int = randint(3, 5)
    main(grid_size, randint(1, grid_size), randint(1, grid_size))
