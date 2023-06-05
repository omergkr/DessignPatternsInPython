"""
You are given two types, Circle and Square, and a decorator called ColoredShape.

The decorator adds the color to the string output for a given shape, just as we did in the lecture.

There's a trick though: the decorator now has a resize() method that should resize the underlying shape.
However, only the Circle has a resize() method; the Square does not — do not add it!

You are asked to complete the implementation of Circle, Square and ColoredShape.

Here is a sample unit test that should pass:

class Evaluate(TestCase):
  def test_circle(self):
    circle = ColoredShape(Circle(5), 'red')
    self.assertEqual(
      'A circle of radius 5 has the color red',
      str(circle)
    )
    circle.resize(2)
    self.assertEqual(
      'A circle of radius 10 has the color red',
      str(circle)
    )
"""


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def resize(self, factor):
        self.radius *= factor

    def __str__(self):
        return f'A circle of radius {self.radius} '


class Square:
    def __init__(self, side):
        self.side = side

    def __str__(self):
        return f"A square of side {self.side} "


class ColoredShape:
    def __init__(self, shape, color):
        self.color = color
        self.shape = shape

    def resize(self, factor):
        if callable(getattr(self.shape, "resize", None)):
            self.shape.resize(factor)

    def __str__(self):
        return f"{self.shape} has the color {self.color}"
