from abc import ABCMeta, abstractmethod
from random import randrange
from dataclasses import dataclass
from operator import itemgetter

class DiceRoller(metaclass=ABCMeta):
    @classmethod
    @abstractmethod
    def roll(self,n,sides,modifier=0):
        pass


class DiceRollResult():
    def __init__(self, result, rolls, modifier=0):
        self.result = result
        self.rolls = rolls
        self.modifier = modifier

    def __str__(self):
        return str(self.result)

    def add(self, modifier):
        return DiceRollResult(
            result=self.result+modifier,
            rolls=self.rolls,
            modifier=self.modifier+modifier,
        )

    

class Die(DiceRoller):
    def roll(n, sides, modifier=0):
        accumulator = 0
        history = []

        for i in range(n):
            dice_roll = randrange(1,sides)
            history.append(dice_roll)
            accumulator += dice_roll

        return DiceRollResult(accumulator, history).add(modifier)

DiceRoller.register(Die)

if(__name__ == "__main__"):
    print(Die.roll(3,6))