"""number guess!"""

CORRECT: int = 8
my_number_string: str = input("guess a number: ")
my_number: int = int(my_number_string)
while my_number != CORRECT:
    if my_number % 2 == 0:
        print("even")
    else:
        print("odd")
    my_number_string = input("guess again: ")
    my_number = int(my_number_string)
print("thanks for playing!")
