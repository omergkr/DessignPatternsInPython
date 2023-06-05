"""
Adding behavior without altering the class itself

Want to augment an object with additional functionality
Do not want to rewrite or alter existing code (OCP - Open Close principle)
Want to keep new functionality separate (SRP - Single Responsibility Principle)
Need to be able to interact with existing structures
Two options:
    - Inherit from required object (if possible)
    - Build a Decorator, which simply references the decorated objects

DECORATOR -> Facilities the addition of behaviours to individual objects without inheriting from them


Summary
A decorator keeps the reference to the decorated objects
Adds utility attributes and methods to augment the object's features
May or may not forward calls to the underlying object
Proxying of underlying calls can be done dynamically
Python's functional decorators wrap functions; no direct relation to the GoF Decorator pattern

"""
import time


def time_it(func):
    def wrapper():
        start = time.time()
        result = func()
        end = time.time()
        print(f"{func.__name__} took {int((end - start) * 1000)}ms")

    return wrapper


@time_it
def some_op():
    print("Starting op")
    time.sleep(1)
    print("We are done")
    return 123


# some_op()
# time_it(some_op)()
some_op()
