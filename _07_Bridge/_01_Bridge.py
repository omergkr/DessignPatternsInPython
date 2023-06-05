"""
Connecting components together through abstractions

Bridge prevents a "Cartesian product" complexity explosion
     - Example
        * Base class ThreadSchedular
        * Can be preemptive or cooperation
        * Can run on Windows or Unix
        * End up with a 2*2 scenario: WindowPTS, UnixPTS, WindowsCTS, UnixCTS
Bridge pattern avoids the entity explosion

BRIDGE -> A mechanism that decouples an interface (hierarchy) from an implementation (hierarchy)

Summary
Decouple abstraction from implementation
Both can exist as hierarchies
A stronger form of encapsulation
"""

from abc import ABC


# Circles and squares
# Each can be rendered in vector or raster form

class Renderer(ABC):
    def render_circle(self, radius):
        pass


class VectorRenderer(Renderer):
    def render_circle(self, radius):
        print(f'Drawing a circle of radius {radius}')


class RasterRenderer(Renderer):
    def render_circle(self, radius):
        print(f'Drawing pixels for circle of radius {radius}')


class Shape:
    def __init__(self, renderer):
        self.renderer = renderer

    def draw(self): pass

    def resize(self, factor): pass


class Circle(Shape):
    def __init__(self, renderer, radius):
        super().__init__(renderer)
        self.radius = radius

    def draw(self):
        self.renderer.render_circle(self.radius)

    def resize(self, factor):
        self.radius *= factor


if __name__ == '__main__':
    raster = RasterRenderer()
    vector = VectorRenderer()
    circle = Circle(vector, 5)
    # circle = Circle(raster, 5)
    circle.draw()
    circle.resize(2)
    circle.draw()
