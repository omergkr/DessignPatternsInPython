"""
Components may go in and out of the system at any time.
    - Chat room has participants
    - Players in an MMORPG
it makes no sense for all of these players to have direct preferences to one another.
    - Those references may go dead
Solution: have them all refer to some central component that facilitates communication.

MEDIATOR -> A component which facilitates communication between other components without them necessarily
being aware of each other or having direct (reference) access to each other


SUMMARY
Create a mediator which will be referenced by every single object, which requires that typically is in a property.
You want to stick the mediator right inside the initializes so nobody forgets to initialize their mediator.
Mediator engages in bidirectional communication with the connected components.
Mediator has functions the components can call
on the other hand, the components have functions that the mediator can call so they know about one another.
Event processing (e.g Rx) libraries make communication easier to implement
"""


class Person:
    def __init__(self, name):
        self.name = name
        self.chat_log = []
        self.room = None

    def receive(self, sender, message):
        s = f'{sender}: {message}'
        print(f'[{self.name}\'s chat session] {s}')
        self.chat_log.append(s)

    def say(self, message):
        self.room.broadcast(self.name, message)

    def private_message(self, who, message):
        self.room.message(self.name, who, message)


class ChatRoom:
    def __init__(self):
        self.people = []

    def broadcast(self, source, message):
        for p in self.people:
            if p.name != source:
                p.receive(source, message)

    def join(self, person):
        join_msg = f'{person.name} joins the chat'
        self.broadcast('room', join_msg)
        person.room = self
        self.people.append(person)

    def message(self, source, destination, message):
        for p in self.people:
            if p.name == destination:
                p.receive(source, message)


room = ChatRoom()

omer = Person('Omer')
orhan = Person('Orhan')

room.join(omer)
room.join(orhan)

omer.say('hi room')
orhan.say('oh, hey Omer')


enes = Person('Enes')
room.join(enes)
enes.say('hi everyone!')

orhan.private_message('Enes', 'glad you could join us!')
