"""
Space optimization, so it's something that tries to save your memory

Avoid redundancy when storing data
E.g MMORPG (massively multiplayer online role-playing games)
    - Plenty of users with identical first/last name
    - No sense in storing same first/last name over and over again
    - Store a list of names and references to them
E.g bold or italic text formatting
    - Don't want each character to have a formatting character
    - Operate on ranges ( line number, start end point)

FLYWEIGHT -> A space optimization technique that lets us use less memory by storing
externally the data associated with similar objects

Summary
Store common data externally
Specify an index or a reference into the external data store
Define the idea of "ranges" on homogeneous collections and store data related to those ranges


"""
import random
import string


class User:
    def __init__(self, name):
        self.name = name


class User2:
    strings = []

    def __init__(self, full_name):
        def get_or_add(s):
            if s in self.strings:
                return self.strings.index(s)
            else:
                self.strings.append(s)
                return len(self.strings) - 1

        self.names = [get_or_add(x) for x in full_name.split(" ")]

    def __str__(self):
        return ' '.join([self.strings[x] for x in self.names])


def random_string():
    chars = string.ascii_lowercase
    return "".join([random.choice(chars) for x in range(8)])


users = []
first_names = [random_string() for x in range(100)]
last_names = [random_string() for y in range(100)]

for first in first_names:
    for last in last_names:
        users.append(User(f"{first} {last}"))

u2 = User2('Jim Jones')
u3 = User2('Frank Jones')
print(u2.names)
print(u3.names)
print(User2.strings)

users2 = []

for first in first_names:
    for last in last_names:
        users2.append(User2(f'{first} {last}'))

for x in users2:
    print(x)
    print(x.names)
