"""Splitting a dictionary into two lists."""

__author__ = "730631751"


def get_keys(x: dict[str, int]) -> list[str]:
    """Returning a list of keys."""
    y: list[str] = []
    for key in x:
        y.append(key)
    return y


test: dict[str, int] = {"Alabama": 1, "Alaska": 2, "Arizona": 3}
test2: dict[str, int] = {}


def get_values(x: dict[str, int]) -> list[int]:
    """Returning a list of values."""
    y: list[int] = []
    for key in x:
        y.append(x[key])
    return y
