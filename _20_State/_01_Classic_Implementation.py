"""
Fun with Finite State Machines


STATE ->
A pattern where the objects behavior is determined by the state, kind of like my behavior is determined by my state.
For example, if I don't get enough sleep, then I'm going to be particularly groggy.
An object transitions from one state to another (something needs to trigger transition)
A formalized construct which actually manages state and transitions from one state to another is called a state machine.

Summary
    - Given sufficient complexity, it's actually useful to define formally define the states as well as the possible
    - We can certainly define the behaviors of state entry and exit,
    - We can define the behaviors that occur as you enter, enter a particular state or as you exit a particular state.
    - You can also customize the state machine in terms of actions
      that are done when a particular event causes and transition, transitions from one state to another.
    - You can define guard conditions for enabling or disabling particular transitions.
    - You can define default actions when no transitions are found for an event.

"""
from abc import ABC


class Switch:
    def __init__(self):
        self.state = OffState()

    def on(self):
        self.state.on(self)

    def off(self):
        self.state.off(self)


class State(ABC):
    def on(self, switch):
        print('Light is already on')

    def off(self, switch):
        print('Light is already off')


class OnState(State):
    def __init__(self):
        print('Light turned on')

    def off(self, switch):
        print('Turning light off...')
        switch.state = OffState()


class OffState(State):
    def __init__(self):
        print('Light turned off')

    def on(self, switch):
        print('Turning light on...')
        switch.state = OnState()


sw = Switch()

sw.on()  # Turning light on...
# Light turned on

sw.off()  # Turning light off...
# Light turned off

sw.off()  # Light is already off
