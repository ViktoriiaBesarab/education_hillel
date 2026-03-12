class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_square(self):
        return self.width * self.height

    def __eq__(self, other):
        return self.width == other.width and self.height == other.height

    def __add__(self, other):
        total_square = self.get_square() + other.get_square()
        return Rectangle(total_square, 1)

    def __mul__(self, n):
        return Rectangle(self.width * n, self.height * n)

    def __str__(self):
        return f'{self.width} x {self.height}'


r1 = Rectangle(2, 4)
r2 = Rectangle(3, 6)
assert r1.get_square()
assert r2.get_square()

r3 = r1 + r2
assert r3.get_square()
print(r3)

r4 = r1 * 4
assert r4.get_square()

assert Rectangle(3, 6)
