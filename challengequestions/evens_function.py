"""Challenge Question 02!"""

__author__ = "730631751"


def display_evens(mynum: int) -> int:
    """Printing all evens less than an input."""
    x: int = mynum
    while mynum >= 0:
        if mynum % 2 == 0:
            print(mynum)
        mynum -= 1
    return x
