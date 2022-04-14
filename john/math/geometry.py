import typing as T
from math import pi

Number = T.Union[int, float]

def circle_area(diameter: Number) -> float:
    radius = diameter / 2
    return pi * (radius ** 2)


def rectangle_area(length: Number, width: Number) -> Number:
    # if isinstance(length, (int, float)):
    return length * width
