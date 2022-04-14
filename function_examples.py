from math import pi
import typing as T

def hello() -> None:
    print("Hello, JPMC world")

x = hello()
print("x: {}".format(x))

Number = T.Union[int, float]

def circle_area(diameter: Number) -> float:
    radius = diameter / 2
    return pi * (radius ** 2)

a = circle_area(50)
print("a: {}".format(a))

print(circle_area(8))


def rectangle_area(length: Number, width: Number) -> Number:
    # if isinstance(length, (int, float)):
    return length * width

print(rectangle_area(5, 12))
a = rectangle_area(14.9, 13.1)
print("a: {}".format(a))
print(rectangle_area('BOSH', 5))

def wacky(p1, p2="wombat"):
    print("p1: {}".format(p1))
    print("p2: {}".format(p2))


wacky('a', 'b')
wacky('a')

def more_wacky(p1, /, p2, *p3, p4, p5, **p6):
    pass



