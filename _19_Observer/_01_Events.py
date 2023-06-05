"""
I am watching you!

We need to be informed when a certain thing happen and that can be virtually anything.
    - object property changes and we need to be informed about those
    - changes might be disallowed, for example, or some of those changes might trigger other things in the system.
    - we might want to watch for is whenever an object does something.
    - you might have some external event that might occur outside the system that you're programming
We want to be able to listen to events and to be notified when those events actually occur.
    - Notifications typically should include all the useful information about the event.
        -  Who generated the event?
        -  What values were generated as part of this event?
We also want to be able to unsubscribe from events, if we're no longer interested

OBSERVER ->  observer is the object that wishes to be informed about something else happening in the system.
And the entity which actually generates those events, which we want to observe, is typically called an observable.
The observable is the generator of the events,
and the observer is the consumer of the events that get the notifications and can decide on what to do with them.
"""


class Event(list):
    def __call__(self, *args, **kwargs):
        for item in self:
            item(*args, **kwargs)


class Person:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.falls_ill = Event()

    def catch_a_cold(self):
        self.falls_ill(self.name, self.address)


def call_doctor(name, address):
    print(f'{name} needs a doctor at {address}')


person = Person('Omer', 'Driessendorfer Str. 69')
person.falls_ill.append(lambda name, addr: print(f'{name} is ill'))
person.falls_ill.append(call_doctor)
person.catch_a_cold()

# and you can remove subscriptions too
person.falls_ill.remove(call_doctor)
person.catch_a_cold()