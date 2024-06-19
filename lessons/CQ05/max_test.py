__author__ = "730631751"

from lessons.CQ05.find_max import find_and_remove_max


def test_find_and_remove_max_return() -> None:
    """Ensuring a correct return value."""
    assert find_and_remove_max([5, 6, 7, 8]) == 8


def test_find_and_remove_max_mutate() -> None:
    """Ensuring accurate mutation."""
    y: list[int] = [5, 6, 7, 8]
    find_and_remove_max(y)
    assert y == [5, 6, 7]


def test_find_and_remove_max_edge() -> None:
    """Observing an instance of an edge case."""
    assert find_and_remove_max([]) == -1
