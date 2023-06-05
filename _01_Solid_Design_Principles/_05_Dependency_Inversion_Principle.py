"""
High level classes or modules in your code should not depend directly on low level modules
Instead, they should depend on abstractions
"""
from abc import abstractmethod
from enum import Enum


class Relationship(Enum):
    PARENT = 0
    CHILD = 1
    SIBLING = 2


class Person:
    def __init__(self, name):
        self.name = name


class RelationshipBrowser:
    @abstractmethod
    def find_all_children_of(self, name): pass


class Relationships(RelationshipBrowser):  # low level module

    def __init__(self):
        self.relations = []  # we can use later database oder other storage type

    def add_parent_and_children(self, parent, child):
        self.relations.append((parent, Relationship.PARENT, child))
        self.relations.append((child, Relationship.CHILD, parent))

    def find_all_children_of(self, name):
        for r in self.relations:
            if r[0].name == name and r[1] == Relationship.PARENT:
                yield r[2].name


class Research:  # high level model

    # dependency on a low-level module directly
    # bad because strongly dependent on e.g. storage type (relations list)

    # def __init__(self, relationships):
    #     relations = relationships.relations
    #     for r in relations:
    #         if r[0].name == 'Omer' and r[1] == Relationship.PARENT:
    #             print(f'Omer has a child called {r[2].name}.')

    def __init__(self, browser):
        for p in browser.find_all_children_of("Omer"):
            print(f"Omer has a child called {p}")


parent = Person("Omer")
child1 = Person("Orhan")
child2 = Person("Enes")

relationships = Relationships()

relationships.add_parent_and_children(parent, child1)
relationships.add_parent_and_children(parent, child2)

Research(relationships)
