"""
Iteration or traversal is a core functionality of various data structures.
An iterator is typically a class that actually facilitates the traversal.
    - Iterator keeps a reference to the current element.
    - Knows how to move from the current element
The iterator protocol requires two things.
    - __iter__() to expose the iterator, which uses
    - __next__() to return each of the iterated elements
    - raise StopIteration when it's done

ITERATOR -> An object that facilitates the traversal of a data structure

Summary
An iterator basically specifies how you can traverse a particular object and stateful iterators.
Stateful iterators cannot be recursive
yield allows for much more succinct and much more understandable implementation of the iteration process.
"""


class Node:
    def __init__(self, value, left=None, right=None):
        self.right = right
        self.left = left
        self.value = value

        self.parent = None

        if left:
            self.left.parent = self
        if right:
            self.right.parent = self

    def __iter__(self):
        return InOrderIterator(self)


class InOrderIterator:
    def __init__(self, root):
        self.root = self.current = root
        self.yielded_start = False
        while self.current.left:
            self.current = self.current.left

    def __next__(self):
        if not self.yielded_start:
            self.yielded_start = True
            return self.current

        if self.current.right:
            self.current = self.current.right
            while self.current.left:
                self.current = self.current.left
            return self.current
        else:
            p = self.current.parent
            while p and self.current == p.right:
                self.current = p
                p = p.parent
            self.current = p
            if self.current:
                return self.current
            else:
                raise StopIteration


def traverse_in_order(root):
    def traverse(current):
        if current.left:
            for left in traverse(current.left):
                yield left
        yield current
        if current.right:
            for right in traverse(current.right):
                yield right

    for node in traverse(root):
        yield node


if __name__ == '__main__':
    #   1
    #  / \
    # 2   3

    # in-order: 213
    # preorder: 123
    # postorder: 231

    root = Node(1, Node(2), Node(3))

    it = iter(root)

    print([next(it).value for x in range(3)])

    for x in root:
        print(x.value)

    for y in traverse_in_order(root):
        print(y.value)
