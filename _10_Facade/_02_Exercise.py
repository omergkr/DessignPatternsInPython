"""
A magic square is a square matrix of numbers where the sum in each row, each column, and each of the diagonals is the same.

You are given a system of 3 classes that can be used to make a magic square. The classes are:

Generator: this class generates a 1-dimensional list of random digits in range 1 to 9.

Splitter: this class takes a 2D list and splits it into all possible arrangements of 1D lists.
It gives you the columns, the rows and the two diagonals.

Verifier: this class takes a 2D list and verifies that the sum of elements in every sublist is the same.

Please implement a Façade class called MagicSquareGenerator  which simply generates the magic square of a given size.
"""

from random import randint


class Generator:
    def generate(self, count):
        return [randint(1, 9) for x in range(count)]


class Splitter:
    def split(self, array):
        result = []

        row_count = len(array)
        col_count = len(array[0])

        for r in range(row_count):
            the_row = []
            for c in range(col_count):
                the_row.append(array[r][c])
            result.append(the_row)

        for c in range(col_count):
            the_col = []
            for r in range(row_count):
                the_col.append(array[r][c])
            result.append(the_col)

        diag1 = []
        diag2 = []

        for c in range(col_count):
            for r in range(row_count):
                if c == r:
                    diag1.append(array[r][c])
                r2 = row_count - r - 1
                if c == r2:
                    diag2.append(array[r][c])

        result.append(diag1)
        result.append(diag2)

        return result


class Verifier:
    def verify(self, arrays):
        first = sum(arrays[0])

        for i in range(1, len(arrays)):
            if sum(arrays[i]) != first:
                return False

        return True


class MagicSquareGenerator:
    def generate(self, size):
        while True:
            magic_square = []
            generator = Generator()
            sp = Splitter()
            v = Verifier()
            for x in range(size):
                magic_square.append(generator.generate(size))

            if v.verify(sp.split(magic_square)):
                break

        return magic_square


gen = MagicSquareGenerator()
square = gen.generate(3)
print(square)
