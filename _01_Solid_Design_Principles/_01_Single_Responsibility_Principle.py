"""
SRP
SOC separation of concerns
A class should only have one reason to change
Separation of concern - different classes handling different, independent tasks/problems
"""


class Journal:

    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        self.count += 1
        self.entries.append(f"{self.count} : {text}")

    def remove_entry(self, pos):
        del self.entries[pos]

    def __str__(self):
        return "\n".join(self.entries)


# we can give the responsibility of saving to another class
"""
    def save(self, filename):
        file = open(filename, "w")
        file.write(str(self))
        file.close()

    def load(self, filename):
        pass

    def load_from_web(self, uri):
        pass
"""


class PersistenceManager:
    def save_to_file(self, journal, filename):
        my_file = open(filename, "w")
        my_file.write(str(journal))
        my_file.close()


j = Journal()
j.add_entry("I cried today.")
j.add_entry("I ate a bug.")
print(f"Journal entries:\n{j}\n")

p = PersistenceManager()
file_name = r'journal.txt'
p.save_to_file(j, file_name)

# verify!
with open(file_name) as fh:
    print(fh.read())
