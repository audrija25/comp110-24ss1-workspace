__author__ = "730631751"


def find_and_remove_max(x: list[int]) -> int:
    """Finding and removing the largest integer in a list."""
    max_elem: int = 0
    idx: int = 0
    if x == []:
        return -1
    else:
        for elem in x:
            if elem > max_elem:
                max_elem = elem
        while idx < len(x):
            if x[idx] == max_elem:
                x.pop(idx)
            else:
                idx += 1
    return max_elem
