"""Making a recursive function."""

__author__ = "730631751"


def f(n: int, k: int) -> int:
    """Multiplying n and k recursively."""
    if n == 0:  # base case
        return n
    else:  # recursive rule
        return k + f(n - 1, k)
