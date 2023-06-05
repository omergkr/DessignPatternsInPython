"""
SINGLETON

For some component it only makes sense to have one in the system
    - Database repository
    - Object factory
The initializer call is expensive
    - We only do it once
    - We provide everyone with the same instance
Want to prevent anyone creating additional copies
Need to take care of lazy instantiation

SINGLETON -> A component which is instantiated only once

Summary
Different realization of Singleton: custom allocator, decorator, metaclass
Laziness is easy, just init on first request
Monostate variation
Testability issues

"""

import random


class Database:
    initialized = False

    def __init__(self):
        self.id = random.randint(1, 101)
        print('Generated an id of ', self.id)
        print('Loading database from file')
        pass

    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Database, cls) \
                .__new__(cls, *args, **kwargs)

        return cls._instance


database = Database()


d1 = Database()
d2 = Database()

print(d1.id, d2.id)
print(d1 == d2)
print(database == d1)
