"""
Strategy Coding Exercise
Consider the quadratic equation and its canonical solution:



The part b^2-4*a*c is called the discriminant.
Suppose we want to provide an API with two different strategies for calculating the discriminant:

In OrdinaryDiscriminantStrategy , If the discriminant is negative, we return it as-is.
This is OK, since our main API returns Complex  numbers anyway.

In RealDiscriminantStrategy , if the discriminant is negative, the return value is NaN (not a number).
NaN propagates throughout the calculation, so the equation solver gives two NaN values.
In Python, you make such a number with float('nan').

Please implement both of these strategies as well as the equation solver itself.
In regard to plus-minus in the formula, please return the + result as the first element and - as the second.
Note that the solve() method is expected to return complex values.
"""

import cmath
from abc import ABC


class DiscriminantStrategy(ABC):
    def calculate_discriminant(self, a, b, c):
        pass


class OrdinaryDiscriminantStrategy(DiscriminantStrategy):
    def calculate_discriminant(self, a, b, c):
        return b*b - 4*a*c


class RealDiscriminantStrategy(DiscriminantStrategy):
    def calculate_discriminant(self, a, b, c):
        result = b*b-4*a*c
        return result if result >= 0 else float('nan')


class QuadraticEquationSolver:
    def __init__(self, strategy):
        self.strategy = strategy

    def solve(self, a, b, c):
        """ Returns a pair of complex (!) values """
        disc = complex(self.strategy.calculate_discriminant(a, b, c), 0)
        root_disc = cmath.sqrt(disc)
        return (
            (-b + root_disc) / (2 * a),
            (-b - root_disc) / (2 * a)
        )


strategy = OrdinaryDiscriminantStrategy()
solver = QuadraticEquationSolver(strategy)
results = solver.solve(1, 10, 16)