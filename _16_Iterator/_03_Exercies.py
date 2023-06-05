"""
Iterator Coding Exercise
Given the following definition of a Node , please implement preorder traversal right inside Node.
The sequence returned should be the sequence of values, not their containing nodes.

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

    def traverse_preorder(self):
        yield self.value
        if self.left:
            yield from self.left.traverse_preorder()
        if self.right:
            yield from self.right.traverse_preorder()


node = Node('a',
            Node('b',
                 Node('c'),
                 Node('d')),
            Node('e'))

print(''.join([x for x in node.traverse_preorder()]))
