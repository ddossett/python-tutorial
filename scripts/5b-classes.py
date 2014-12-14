# Let's try something more fun, creating logic for video game characters.
# Define a class for a character in the game.

class Character:
    """Basic character class containing a few simple interactions"""

    def __init__(self, name, hp, attack):
        self.name = name
        self.hp = hp
        self.attack_power = attack
        self.status = "Alive"

    def attack(self, target):
        """Allows us to deal our attack damage to another character
        instance"""
        target.take_damage(self.attack_power)

    def take_damage(self, damage): 
        """Reduce hp by the amount of damage taken"""
        self.hp -= damage 
        print(self.name,"took",damage,"points of damage")
        if self.hp <= 0:
            self.hp = 0
            self.status = "Dead"
            print(self.name,"died!")

    def isdead(self): 
        """Checks the status of the character for death, status should
        have been updated by other methods when death occurred."""
        if self.status == "Alive":
            return False
        else:
            return True

# Create two characters, I'm using keyword arguments for readability but
# it's not necessary.
finn = Character(name="Finn", hp=10, attack=3) 
goblin = Character(name="Uzog", hp=4, attack=3)

# Can access their member variables.
print()
print(finn.name, "is", finn.status)
print(goblin.name, "is", goblin.status)
print()

# They battle until one is dead
while True:
    finn.attack(goblin)
    if goblin.isdead():
        print(finn.name,"has",finn.hp,"hp")
        break
    goblin.attack(finn)
    if finn.isdead():
        print(goblin.name,"has",goblin.hp,"hp")
        break
    print(goblin.name,"has",goblin.hp,"hp")
    print(finn.name,"has",finn.hp,"hp\n")

# Notice how the information about each character was stored by each variable
# making it easier to see what is going on. The fight logic is small and easy
# to understand once the class is made because we've divorced the fight from
# the character information.

# We could easily make huge numbers of characters with their own stats and it'd
# be vastly easier to keep track of, rather than using lots of separate lists or
# dictionaries for character names, attack, status, hp etc.

# However, remember to be sensible and only use classes when it makes sense to.
