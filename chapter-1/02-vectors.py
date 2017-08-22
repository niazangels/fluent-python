from math import hypot


class Vector:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Vector ({}, {})'.format(self.x, self.y)

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def __abs__(self):
        return hypot(self.x, self.y)

    def __bool__(self):
        return(hypot(self.x, self.y))


if __name__ == '__main__':
    a = Vector(1, 1)
    b = Vector(2, 2)

    print('a = {}'.format(a))
    print('b = {}'.format(b))

    print('\nAddition')
    print('a + b = {}'.format(a + b))

    print('\nSubtaction by addition and sneaky multiplication')
    print('b - a = {}'.format(a + b * -1))

    print('\nTruthy of the above sneaky subtraction')
    print('b - a = {}'.format(bool(a + b * -1)))

    print('\nAbsolute of {}'.format(a))
    print(abs(a))
