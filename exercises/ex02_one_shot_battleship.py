"""One Shot Battleship!"""

__author__ = "730631751"

grid_size: int = 4
secret_row: int = 3
secret_column: int = 2
row_input_str: str = input("Guess a row: ")
row_input: int = int(row_input_str)
column_input_str: str = input("Guess a column: ")
column_input: int = int(column_input_str)
BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"
row_counter: int = 1

result_box: str = ""
if column_input == secret_column and row_input == secret_row:
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


while row_input < 1 or row_input > grid_size:
    new_row_input: str = input(
        f"The grid is only {grid_size} by {grid_size}. Try again: "
    )
    row_input = int(new_row_input)

while column_input < 1 or column_input > grid_size:
    new_column_input: str = input(
        f"The grid is only {grid_size} by {grid_size}. Try again: "
    )
    column_input = int(new_column_input)

if row_input == secret_row and column_input == secret_column:
    print("Hit!")
elif row_input == secret_row and column_input != secret_column:
    print("Close! Correct row, wrong column.")
elif column_input == secret_column and row_input != secret_column:
    print("Close! Correct column, wrong row.")
else:
    print("Miss!")
