from abc import ABCMeta, abstractmethod
from random import randrange

class DiceRoller(metaclass=ABCMeta):
    @classmethod
    @abstractmethod
    def roll(self,n,sides):
        pass

class Die(DiceRoller):
    def roll(n, sides):
        accumulator = 0
        history = []
        for i in range(n):
            dice_roll = randrange(1,sides)
            history.append(dice_roll)
            accumulator += dice_roll
        return {"result": accumulator, "rolls": history}

DiceRoller.register(Die)

if(__name__ == "__main__"):
    print("Hello, world!")
    print(issubclass(Die, DiceRoller))
    print(Die.roll(3,6))