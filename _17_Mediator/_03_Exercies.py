"""
Mediator Coding Exercise
Our system has any number of instances of Participant  classes.
Each Participant has a value integer attribute, initially zero.

A participant can say()  a particular value, which is broadcast to all other participants.
At this point in time, every other participant is obliged to increase their value  by the value being broadcast.

Example:

Two participants start with values 0 and 0 respectively

Participant 1 broadcasts the value 3. We now have Participant 1 value = 0, Participant 2 value = 3

Participant 2 broadcasts the value 2. We now have Participant 1 value = 2, Participant 2 value = 3
"""


class Event(list):
    def __call__(self, *args, **kwargs):
        for item in self:
            item(*args, **kwargs)


class Participant:
    def __init__(self, mediator):
        self.value = 0
        self.mediator = mediator
        mediator.alert.append(self.mediator_alert)

    def say(self, value):
        self.mediator.broadcast(self, value)

    def mediator_alert(self, sender, value):
        if sender != self:
            self.value += value


class Mediator:
    def __init__(self):
        self.alert = Event()

    def broadcast(self, sender, value):
        self.alert(sender, value)


m = Mediator()
p1 = Participant(m)
p2 = Participant(m)

p1.say(10)
print(p1.value)
print(p2.value)

p2.say(5)
print(p1.value)
print(p2.value)