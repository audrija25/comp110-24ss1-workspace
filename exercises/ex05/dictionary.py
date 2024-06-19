"""Working with dictionaries."""

__author__ = "730631751"


def count(x: list[str]) -> dict[str, int]:
    """Counting over elements in a dictionary."""
    storage: dict[str, int] = {}
    for elem in x:
        if elem in storage:
            storage[elem] += 1
        else:
            storage[elem] = 1
    return storage


def alphabetizer(x: list[str]) -> dict[str, list[str]]:
    """Assign each string an initial."""
    storage: dict[str, list[str]] = {}
    for word in x:
        initial: str = word[0].lower()
        if initial in storage:
            storage[initial].append(word)
        else:
            storage[initial] = [word]
    return storage


def invert(x: dict[str, str]) -> dict[str, str]:
    """Inverting the key and value."""
    y: dict[str, str] = {}
    for keys in x:
        values: str = x[keys]
        if values in y:
            raise KeyError("Duplicate key, cannot proceed.")
        y[x[keys]] = keys
    return y


def favorite_color(x: dict[str, str]) -> str:
    """Identifying the most frequently appearing color."""
    storage: dict[str, int] = {}
    if x == {}:
        return ""
    for elem in x:
        if x[elem] in storage:
            storage[x[elem]] += 1
        else:
            storage[x[elem]] = 1
    print(storage)
    counter: int = 0
    fav_colors: list[str] = []
    for colors in storage:
        if storage[colors] > counter:
            counter = storage[colors]
            fav_colors.append(colors)
    fav_color: str = fav_colors[len(fav_colors) - 1]
    print(fav_colors)
    return fav_color


test: dict[str, str] = {"a": "b", "c": "d", "e": "b"}
test2: dict[str, str] = {"a": "b", "c": "d", "e": "b", "f": "d"}
favorite_color(test)
favorite_color(test2)


def update_attendance(x: dict[str, list[str]], y: str, z: str) -> None:
    """Updating a class's attendance."""
    if y in x:
        if z not in x[y]:
            x[y].append(z)
    else:
        x[y] = [z]
