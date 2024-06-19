"""Mutating functions."""

__author__ = "730631751"


# part 1: defining my_append
def manual_append(x: list[int], a: int) -> None:
    """Defining a manual append."""
    x.append(a)


# part 2: defining double
def double(x: list[int]) -> None:
    """Defining a double."""
    idx: int = 0
    while idx < len(x):
        x[idx] *= 2
        idx += 1
