class Event(list):
    def __call__(self, *args, **kwargs):
        for item in self:
            item(*args, **kwargs)


class Game:
    def __init__(self):
        self.events = Event()

    def fire(self, args):
        self.events(args)


class GoalScoredInfo:
    def __init__(self, who_scored, goals_scored):
        self.goals_scored = goals_scored
        self.who_scored = who_scored


class Player:
    def __init__(self, name, game):
        self.name = name
        self.game = game
        self.goals_scored = 0

    def score(self):
        self.goals_scored += 1
        args = GoalScoredInfo(self.name, self.goals_scored)
        self.game.fire(args)


class Coach:
    def __init__(self, game):
        game.events.append(self.celebrate_goal)

    def celebrate_goal(self, args):
        if isinstance(args, GoalScoredInfo) and args.goals_scored < 3:
            print(f'Coach says: well done, {args.who_scored}!')


game = Game()
player = Player('Omer', game)
coach = Coach(game)

player.score()  # Coach says: well done, Sam!
player.score()  # Coach says: well done, Sam!
player.score()  # ignored by coach

"""
the celebrate_goal function() is a method of the Coach class. Inside the __init__ method of the Coach class, 
the line game.events.append(self.celebrate_goal) adds the celebrate_goal method to the game.events list.

game.events is an instance of the Event class, 
so when the __call__ method of the Event class is called (self.events(args)), 
it iterates over the items in the Event instance, which is essentially a list (since it inherits from the list class), 
and calls each item with the args and kwargs arguments.

In this case, when player.score() method is called, 
it executes the score method in the Player class, 
which in turn executes the line self.game.fire(args). 
invokes the fire method of the game object and passes the args argument. 
As a result, the fire method iterates over the items in the game.events list and calls each item with the args argument.

Since the celebrate_goal function is present in the game.events list, 
the celebrate_goal function receives the args argument and checks if it is an instance of the GoalScoredInfo class.
If args is an instance of GoalScoredInfo and args.goals_scored is less than 3, 
the celebrate_goal function prints "Coach says: well done, {args.who_scored}!".
"""