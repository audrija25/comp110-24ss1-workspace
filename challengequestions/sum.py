"""Summing the elements of a list using different loops."""

__author__ = "730631751"


# part 1: w_sum
def w_sum(vals: list[float]) -> float:
    """Calculating the sum of a list's elements."""
    idx: int = 0
    count: float = 0.0
    while idx < len(vals):
        count += vals[idx]
        idx += 1
    return count


# part 2: f_sum
def f_sum(vals: list[float]) -> float:
    """Using a for loop to achieve the same result."""
    count: float = 0.0
    for elem in vals:
        count += elem
    return count


# part 3: f_range_sum
def f_range_sum(vals: list[float]) -> float:
    """Using a for loop with range to achieve the same result."""
    count: float = 0.0
    for idx in range(0, len(vals)):
        count += vals[idx]
    return count


# x: list[float] = [0.1, 0.2, 0.3]
# y: float = w_sum(x)
# print(y)
