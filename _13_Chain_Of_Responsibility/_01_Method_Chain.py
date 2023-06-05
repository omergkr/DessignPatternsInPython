"""
Chain of Responsibility

Sequence of handlers processing ab event after another

Unethical behaviour by an employee; who takes the blame?
    - Employee
    - Manager
    - CEO
You click a graphical element on a form
    - Button handles it, stops further processing
    - Underlying group box
    - Underlying window
CCG computer game
    - Creature has attack and defense values
    - Those can be boosted by other cards

CHAIN OF RESPONSIBILITY -> A chain of components who all get a chance to process a command or a query,
optionally having default processing implementation and an ability to terminate the processing chain


Summary
Chain of Responsibility can be implemented as a chain of references or a centralized construct
Enlist objects in the chain, possibly controlling their order
Object removal from chain (e,g ib __exit__)
"""


class Creature:
    def __init__(self, name, attack, defense):
        self.defense = defense
        self.attack = attack
        self.name = name

    def __str__(self):
        return f'{self.name} ({self.attack}/{self.defense})'


class CreatureModifier:
    def __init__(self, creature):
        self.creature = creature
        self.next_modifier = None

    def add_modifier(self, modifier):
        if self.next_modifier:
            self.next_modifier.add_modifier(modifier)
        else:
            self.next_modifier = modifier

    def handle(self):
        if self.next_modifier:
            self.next_modifier.handle()


class NoBonusesModifier(CreatureModifier):
    def handle(self):
        print('No bonuses for you!')


class DoubleAttackModifier(CreatureModifier):
    def handle(self):
        print(f'Doubling {self.creature.name}''s attack')
        self.creature.attack *= 2
        super().handle()


class IncreaseDefenseModifier(CreatureModifier):
    def handle(self):
        if self.creature.attack <= 2:
            print(f'Increasing {self.creature.name}''s defense')
            self.creature.defense += 1
        super().handle()


goblin = Creature('Goblin', 1, 1)
print(goblin)

root = CreatureModifier(goblin)

root.add_modifier(NoBonusesModifier(goblin))

root.add_modifier(DoubleAttackModifier(goblin))
root.add_modifier(DoubleAttackModifier(goblin))

# no effect
root.add_modifier(IncreaseDefenseModifier(goblin))

root.handle()  # apply modifiers
print(goblin)
