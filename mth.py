from math import pi

# -- AREA -- #
def square_area(a):
        """Calculate cube area"""
        return pow(a, 2)


def rect_area(a, b):
        """Calculate rectangle area"""
        return a*b


def circle_area(r):
        """Calculate circle area"""
        return pi*pow(r, 2)


# -- PERIMETER -- #

def square_perimeter(a):
        """Calculate square perimeter"""
        return a*2


def rect_perimeter(a, b):
        return a+b


def circle_perimeter(r):
        """Calculate circle area"""  # Это я добавил бтв
        return 2*3,14*r
