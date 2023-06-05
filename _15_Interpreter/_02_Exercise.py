"""
Interpreter Coding Exercise

You are asked to write an expression processor for simple numeric expressions with the following constraints:

Expressions use integral values (e.g., '13' ),
single-letter variables defined in Variables, as well as + and - operators only

There is no need to support braces or any other operations

If a variable is not found in variables  (or if we encounter a variable with >1 letter, e.g. ab),
the evaluator returns 0 (zero)

In case of any parsing failure, evaluator returns 0

Example:

calculate("1+2+3")  should return 6

calculate("1+2+xy")  should return 0

calculate("10-2-x")  when x=3 is in variables  should return 5
"""
import re
from enum import Enum


class ExpressionProcessor:
    class Type(Enum):
        PLUS = 1
        MINUS = 2

    def __init__(self):
        self.variables = {}

    def calculate(self, expression):
        current = 0
        next_op = None

        parts = re.split('(?<=[+-])', expression)

        for part in parts:
            noop = re.split('[\+\-]', part)
            first = noop[0]
            value = 0

            try:
                value = int(first)
            except ValueError:
                if len(first) == 1 and first[0] in self.variables:
                    value = self.variables[first[0]]
                else:
                    return 0

            if not next_op:
                current = value
            elif next_op == self.Type.PLUS:
                current += value
            elif next_op == self.Type.MINUS:
                current -= value

            if part.endswith('+'):
                next_op = self.Type.PLUS
            elif part.endswith('-'):
                next_op = self.Type.MINUS

        return current


ep = ExpressionProcessor()
ep.variables['x'] = 5

print(ep.calculate('1+2'))
print(ep.calculate('1+x'))
print(ep.calculate('1+xy'))
