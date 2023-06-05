"""
PROTOTYPE

Complicated objects (e.g cars) aren't designed from scratch
    - They reiterate existing designs
An existing (partially or fully constructed) design is a Prototype
We make a copy(clone) the prototype and customize it
    -Requires deep copy support
We make the cloning convenient (e.g via a Factory)

PROTOTYPE -> A partially or fully initialized object that you copy (clone) and make use of.

SUMMARY
To implement a prototype, partially construct an object and store it somewhere
Deep copy the prototype
Customize the resulting instance
A factory provides a convenient API for using prototypes
"""
import copy


class Address:
    def __init__(self, street_address, city, country):
        self.country = country
        self.city = city
        self.street_address = street_address

    def __str__(self):
        return f"{self.street_address}, {self.city}, {self.country}"


class Person:
    def __init__(self, name, address):
        self.address = address
        self.name = name

    def __str__(self):
        return f"{self.name} lives at {self.address}"


omer = Person("Ömer", Address("flora str. 69", "Krefeld", "Germany"))
print(omer)
# jane = omer does not work
jane = copy.deepcopy(omer)  # making a brand-new object that doesn't refer the original
jane.name = "Jane"
jane.address.street_address = "124 London Road"
print(omer)
print(jane)

