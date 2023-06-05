"""
A TokenMachine  is in charge of keeping tokens.
Each Token  is a reference type with a single numerical value.
The machine supports adding tokens and, when it does,
it returns a memento representing the state of that system at that given time.

You are asked to fill in the gaps and implement the Memento design pattern for this scenario.
Pay close attention to the situation where a token is fed in as a reference and
its value is subsequently changed on that reference - you still need to return the correct system snapshot!
"""
from copy import deepcopy


class Token:
    def __init__(self, value=0):
        self.value = value


class Memento(list):
    pass


class TokenMachine:
    def __init__(self):
        self.tokens = []

    def add_token_value(self, value):
        return self.add_token(Token(value))

    def add_token(self, token):
        self.tokens.append(token)
        return Memento(deepcopy(self.tokens))

    def revert(self, memento):
        list_of_token = []
        for x in memento:
            list_of_token.append(Token(x.value))

        self.tokens = list_of_token
        # self.tokens = [Token(x.value) for x in memento]


tm = TokenMachine()
m = tm.add_token_value(123)
tm.add_token_value(456)
tm.revert(m)
