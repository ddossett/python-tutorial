import random
random.seed()
randint = random.randint

# We pull in the dice rolling function as an import
# just in case things that aren't characters might need it
import dwtools
roll2d6 = dwtools.roll2d6


class Character:
    """Basic character class to be built on with other character types"""

    def __init__(self, name):
        self.name = name

        # Some default values that may change for sub classes
        self.hp = 10
        self.damage_die = 4
        self.status = "Alive"
        self.xp = 0

        # Creating these dictionaries for changing later
        self.score_modifiers = {1:-3, 2:-3, 3:-3, 4:-2, 5:-2, 6:-1, 7:-1, 8:-1,
                                9:0, 10:0, 11:0, 12:0, 13:1, 14:1, 15:1, 16:2, 17:2, 18:3}
        self.ability_scores = {"STR":1, "DEX":1, "CON":1, "INT":1, "WIS":1, "CHA":1}
        self.modifiers = {}
        self.update_modifiers()

    def deal_damage(self, target):
        damage = randint(1,self.damage_die)
        print(self.name,"dealt",damage,"points of damage to",target.name)
        target.take_damage(damage)

    def take_damage(self, damage):
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
            self.modifiers[ability] = self.score_modifiers[score]

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
            

finn = Character("Finn")
finn.ability_scores = {"STR":16, "DEX":13, "CON":15, "INT":8, "WIS":9, "CHA":12}
finn.update_modifiers()

jake = Character("Jake")
jake.ability_scores = {"STR":16, "DEX":13, "CON":15, "INT":8, "WIS":9, "CHA":12}
jake.update_modifiers()

roll = finn.basic_move("STR")

if roll>=10:
    finn.deal_damage(jake)
elif 9>=roll>=7:
    finn.deal_damage(jake)
    jake.deal_damage(finn)
else:
    jake.deal_damage(finn)
