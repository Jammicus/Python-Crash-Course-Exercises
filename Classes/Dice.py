from random import randint


class die():
    def __init__(self, sides):
        self.sides = sides

    def roll_die(self, numberOfRolls):
        while numberOfRolls != 0:
            print(str(randint(1, self.sides)))
            numberOfRolls = numberOfRolls - 1


print("Rolling a 6 sided dice 10 times")
sixSideDice = die(6)
sixSideDice.roll_die(10)

print("Rolling a 10 sided dice 10 times")
tenSideDice = die(10)
tenSideDice.roll_die(10)
print("Rolling a 20 sided dice 10 times")
twentySideDice = die(20)
twentySideDice.roll_die(10)
