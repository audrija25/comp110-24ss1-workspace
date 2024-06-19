"""Defining a class 'Point'."""

from __future__ import annotations

__author__ = "730631751"


class Point:
    """X and Y coordinates."""

    x: int | float
    y: int | float

    def __init__(self, x_init: int | float, y_init: int | float):
        """Defining the coordinates."""
        self.x = x_init
        self.y = y_init

    def scale_by(self, factor: int) -> None:
        """Scaling up the coordinates one way."""
        self.x *= factor
        self.y *= factor

    def scale(self, factor: int) -> Point:
        """Scaling up the coordinates another way."""
        new_x: float = self.x * factor
        new_y: float = self.y * factor
        new_point: Point = Point(new_x, new_y)
        return new_point

    def __str__(self) -> str:
        """Converting a Point to a string."""
        view_as: str = f"x: {self.x}; y: {self.y}"
        return view_as

    def __mul__(self, mul_factor: int | float) -> Point:
        """Multiplying a Point with a number."""
        return Point(self.x * mul_factor, self.y * mul_factor)

    def __add__(self, add_factor: int | float) -> Point:
        """Adding a number to the x and y of a Point."""
        return Point(self.x + add_factor, self.y + add_factor)


"""my_point: Point = Point(2, 3)
my_point = my_point.__mul__(3)
print(my_point.__str__())"""
