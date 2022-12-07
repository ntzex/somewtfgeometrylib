from math import pi


def square_area(a):
    """Calculate cube area (a^2)"""
    return pow(a, 2)


def rect_area(a, b):
    """Calculate rectangle area (a*b)"""
    return a*b


def circle_area(r):
    """Calculate circle area (pi*r^2)"""
    return pi*pow(r, 2)


def square_perimeter(a):
    """Calculate square perimeter (a*2)"""
    return a*2


def rect_perimeter(a, b):
    """Calculate rectangle perimeter (a+b)"""
    return a+b


def circle_perimeter(r):
    """Calculate circle perimeter (2*pi*r)"""
    return 2*pi*r
