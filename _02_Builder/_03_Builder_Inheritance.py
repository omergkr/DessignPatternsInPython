class Person:
    def __init__(self):
        self.name = None
        self.position = None
        self.date_of_birth = None

    def __str__(self):
        return f'{self.name} born on {self.date_of_birth} works as a {self.position}'

    @staticmethod
    def new():
        # return PersonBuilder()
        return PersonBirthDateBuilder()


class PersonBuilder:
    def __init__(self):
        self.person = Person()

    def build(self):
        return self.person


class PersonInfoBuilder(PersonBuilder):
    def called(self, name):
        self.person.name = name
        return self


class PersonJobBuilder(PersonInfoBuilder):
    def works_as_a(self, position):
        self.person.position = position
        return self


class PersonBirthDateBuilder(PersonJobBuilder):
    def born(self, date_of_birth):
        self.person.date_of_birth = date_of_birth
        return self


pb = PersonBirthDateBuilder()
omer = pb\
    .called("ömer")\
    .works_as_a("QA")\
    .born("11/09/1983")\
    .build()

print(omer)
orhan = Person\
    .new()\
    .called("Orhan")\
    .works_as_a("Student")\
    .born("25.06.2015")\
    .build()

print(orhan)