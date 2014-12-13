# Python supports object oriented code through defining classes.
# Classes are essentially variable types that you can define yourself
# and give them their own data to store and functions (methods) to use.
# This lets you encapsulate information about an object together in one
# variable, rather than having to make more complicated logic that
# keeps track of what information is useful in which circumstances.

# Using classes can greatly reduce the amount of code if used appropriately.

# Let's try something more fun, creating logic for video game characters.

# Define a class for a character in the game.

class Character:
    """Basic character class containing a few simple interactions"""
    # Docstrings work as in functions

    def __init__(self, name, hp, attack):
        # This function is special. You don't need it but it lets you
        # setup the initial values and do some logic when you create
        # a new instance of the class.
        # Here we're setting up some internal data for our character from
        # the arguments passed in. These are called member variables and they
        # start with 'self', meaning that they belong to an instance of the
        # class, not to all of them at once.
        self.name = name
        self.hp = hp
        self.attack = attack
        self.status = "Alive"

    def take_damage(self, damage):    # Can define as many functions as we want
        """Reduce hp by the amount of damage taken"""
        self.hp -= damage   # member variables can be accessed between functions
        if self.hp <= 0:
            self.hp = 0
            self.status = "Dead"

    def dead(self):    # All methods should take a 'self' argument as a first argument
        if self.status == "Alive":
            return False
        else:
            return True

# Create two characters, I'm using keyword arguments for readability but
# it's not necessary.
finn = Character(name="Finn", hp=10, attack=3)  # The arguments are in the __init__()
goblin = Character(name="Uzog", hp=4, attack=3)

# Can access their member variables.
print()
print(finn.name, "is", finn.status)
print(goblin.name, "is", goblin.status)
print()

# They battle until one is dead
while True:
    goblin.take_damage(finn.attack)
    if goblin.dead():   # Can use their methods
        print(goblin.name,"has been slain!")
        print(finn.name,"has",finn.hp,"hp")
        break
    finn.take_damage(goblin.attack)
    if finn.dead():
        print(finn.name,"has been slain!")
        print(goblin.name,"has",goblin.hp,"hp")
        break
    print(finn.name,"has",finn.hp,"hp")
    print(goblin.name,"has",goblin.hp,"hp\n")

# Notice how the information about each character was stored by each variable,
# making it easier to see what is going on.
# Simply changing the attack/hp can let us re-run the fight quickly.

# We could easily make huge numbers of characters with their own stats and it'd
# be vastly easier to keep track of than using lots of separate lists/dictionaries
# for character names, attack, status, hp etc.
