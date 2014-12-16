import dungeonworld   # imports the package and the module names (also runs the __init__.py)
from dungeonworld import characters    # imports the characters module name and runs the code inside
import dungeonworld.dwtools as dwtools  # can import a module with an alias to give a shorter name

Character = characters.Character   # We can define a shorter name by using a variable
Fighter = characters.Fighter
Thief = characters.Thief

finn = Fighter("Finn")
goblin = Character("Uzog")
tiffany = Thief("Tiffany")

print(finn.name,"is a Character:",isinstance(finn, Character))  # Can use isinstance() to check class
print(finn.name,"is a Fighter:",isinstance(finn, Fighter))
print()
print(goblin.name,"is a Character:",isinstance(goblin, Character))
print(goblin.name,"is a Fighter:",isinstance(goblin, Fighter))
print(goblin.name,"is a Thief:",isinstance(goblin, Thief))
print()
print(tiffany.name,"is a Character:",isinstance(tiffany, Character))
print(tiffany.name,"is a Thief:",isinstance(tiffany, Thief))

print()
roll = finn.basic_move("STR")
if roll>=10:
    finn.deal_damage(goblin)
elif 9>=roll>=7:
    finn.deal_damage(goblin)
    goblin.deal_damage(finn)
else:
    goblin.deal_damage(finn)
