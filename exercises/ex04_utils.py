"""Utility of lists."""

__author__ = "730631751"


def all(x: list[int], y: int) -> bool:
    """Does the integer match the list?"""
    idx: int = 0
    if x == []:
        return False
    while idx < len(x):
        if x[idx] != y:
            return False
        idx += 1
        if x[idx] == y:
            return True
        idx += 1


def max(x: list[int]) -> int:
    """Finds the maximum element."""
    max_elem: int = 0
    if x == []:
        raise ValueError("max() arg is an empty list.")
    else:
        for elem in x:
            if elem > max_elem:
                max_elem = elem
    return max_elem


def is_equal(x: list[int], y: list[int]) -> bool:
    """Determine equality of lists."""
    if x == [] and y == []:
        return True
    if x == [] and y != []:
        return False
    if x != [] and y == []:
        return False
    if len(x) != len(y):
        return False
    idx: int = 0
    while idx < len(x) and idx < len(y):
        if x[idx] != y[idx]:
            return False
        idx += 1
    else:
        return True


def extend(x: list[int], y: list[int]) -> None:
    """Extending a list."""
    idx: int = 0
    while idx < len(y):
        x.append(y[idx])
        idx += 1


a: list[int] = [1, 2, 3]
b: list[int] = [4, 5, 6]
