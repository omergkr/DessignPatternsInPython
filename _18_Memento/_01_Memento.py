"""
Keep a memento of an object's state to return to that state

An object in a typical system might go through several changes.
    - you can have a bank account and the bank account has money deposited in it and withdraw.
There are different ways of actually navigating those changes.
One way is to record every change (Command) and teach a command to undo itself
simpler approach is to quite simply save the snapshot of the system at every point in time.
A token/handle representing the system state. Lets us roll back to the state when the token was generated.
May or may not directly expose state information

Summary
Mementos are used to roll back states arbitrarily.
A memento is quite simply a token/handle class with (typically) no functions of its own.
They just store as a piece of data and allows us to roll back to this data.
The memento itself is not required to expose this state to which it reverts the system.
We can use the momentum to implement, for example, the undo and redo operations.
"""


class Memento:
    def __init__(self, balance):
        self.balance = balance


class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return Memento(self.balance)  # !!!
    # !!!
    # we return a memento.
    # So we take the system in its current state and we return a snapshot.

    def restore(self, memento):
        self.balance = memento.balance

    def __str__(self):
        return f'Balance = {self.balance}'


ba = BankAccount(100)
m1 = ba.deposit(50)
m2 = ba.deposit(25)
print(ba)

# restore to m1
ba.restore(m1)
print(ba)

# restore to m2
ba.restore(m2)
print(ba)