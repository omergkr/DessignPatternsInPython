"""
You are given an example of an inheritance hierarchy which results in Cartesian-product duplication.

Please refactor this hierarchy, giving the base class Shape  a constructor that
takes an interface Renderer  defined as

class Renderer(ABC):
    @property
    def what_to_render_as(self):
        return None

as well as VectorRenderer  and RasterRenderer  classes.
Each inheritor of the Shape  abstract class should have a constructor that takes a Renderer
such that, subsequently, each constructed object's __str__()  operates correctly, for example,

str(Triangle(RasterRenderer()) # returns "Drawing Triangle as pixels"
"""
from abc import ABC


class Renderer(ABC):
    @property
    def what_to_render_as(self):
        return None


class Shape(ABC):
    def __init__(self, renderer, name):
        self.renderer = renderer
        self.name = name

    def __str__(self):
        return 'Drawing %s as %s' % (self.name, self.renderer.what_to_render_as)


class Triangle(Shape):
    def __init__(self, renderer):
        super().__init__(renderer, 'Triangle')


class Square(Shape):
    def __init__(self, renderer):
        super().__init__(renderer, 'Square')


class RasterRenderer(Renderer):
    @property
    def what_to_render_as(self):
        return 'pixels'


class VectorRenderer(Renderer):
    @property
    def what_to_render_as(self):
        return 'lines'
