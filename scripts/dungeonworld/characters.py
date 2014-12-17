import random  # This is a nice standard library tool for getting random values
random.seed()
randint = random.randint

import dungeonworld.dwtools as dwtools
roll2d6 = dwtools.roll2d6


class Character:
    """Basic character class to be built on with other character types"""

    # Same value for all instances
    score_modifiers = {1:-3, 2:-3, 3:-3, 4:-2, 5:-2, 6:-1, 7:-1, 8:-1,
                       9:0, 10:0, 11:0, 12:0, 13:1, 14:1, 15:1, 16:2, 17:2, 18:3}
    
    def __init__(self, name):
        self.name = name

        # Some default values that may change for sub classes
        self.hp = 10
        self.damage_die = 4
        self.status = "Alive"
        self.xp = 0

        # Creating these dictionaries for changing later
        self.ability_scores = {"STR":1, "DEX":1, "CON":1, "INT":1, "WIS":1, "CHA":1}
        self.modifiers = {}
        self.update_modifiers()

    def deal_damage(self, target):
        """Rolls for damage based on your damage die"""
        damage = randint(1,self.damage_die)
        print(self.name,"dealt",damage,"points of damage to",target.name)
        target.take_damage(damage)

    def take_damage(self, damage):
        """Reduce hp by an amount given by the damage taken. Checks for hp<=0"""
        self.hp -= damage
        print(self.name,"lost",damage,"hit points")
        if self.hp <= 0:
            self.status = "Unconcious"
            self.hp = 0
            print(self.name,"is unconcious!")

    def update_modifiers(self):
        """Recalculate all the ability modifiers from the ability scores. Useful after
        levelling up."""
        for ability, score in self.ability_scores.items():
            self.modifiers[ability] = Character.score_modifiers[score]

    def basic_move(self, ability=None):
        """Moves in Dungeon World are the basic thing a character can do.
        You roll 2d6+modifier where the modifier depends on the ability (score)
        you are using to make the move."""
        roll = roll2d6()
        if ability is None:
            print(self.name, "rolls", roll, ": Total =",sum(roll))
            return sum(roll)
        else:
            print(self.name, "rolls", str(roll)+"+"+ability+" : Total =",
                  sum(roll)+self.modifiers[ability])
            return sum(roll)+self.modifiers[ability]

#### INHERITANCE ####

# This is good so far, but what if want a specific type of character
# that is very similar to Character() but slightly different?
# In that case it is useful to make a new class which 'inherits'
# from the Character class. Basically we are telling the new class to
# have the same member variables and methods that the parent class has.

# Fighter class

class Fighter(Character):   # This is how we sub-class.  class SubClassName(ParentClassName):
    """Sub-class of Character, Fighter. Implements ability scores, hp, and damage die."""
    def __init__(self, name):
        Character.__init__(self, name)
        # We need this line in this specific case because some important variable
        # values are set in the Character class init method.

        # Fighters now have specific values for ability scores
        self.ability_scores = {"STR":16, "DEX":13, "CON":15, "INT":8, "WIS":9, "CHA":12}
        self.update_modifiers()

        # Fighters have a specific hp and damage
        self.hp = 10+self.ability_scores["CON"]
        self.damage_die = 10

# See how much less code this sub-class has!! It still has all of the member variables
# and methods of the Character class but just a few changes.
# You can override a method/variable simply by making it in the subclass as we did with
# the __init__ method. Note that this meant we had to call the Character __init__
# directly to make sure that the variables in the Character.__init__() were initilised.

class Thief(Character):
    def __init__(self, name):
        Character.__init__(self, name)
        self.ability_scores = {"STR":9, "DEX":16, "CON":12, "INT":15, "WIS":8, "CHA":12}
        self.update_modifiers()
        self.hp = 6+self.ability_scores["CON"]
        self.damage_die = 8
