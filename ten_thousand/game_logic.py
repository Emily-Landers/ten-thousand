from collections import Counter
import random

class GameLogic ():
    


    
    def __init__(self, value):
        self.value = value

#The input to calculate_score is a tuple of integers that represent a dice roll.
#The output from calculate_score is an integer representing the roll’s score according to rules of game.
    @staticmethod     
    def roll_dice(self):
        rolls = [random.randint(1, 6) for _ in range(self)]
        # dice = self.rolls
        # dice.append(rolls)
        return tuple(rolls)

    @staticmethod 
    def calculate_score(rolls, score=[]):
        scores = score
        if 5 in rolls:
            num = rolls.count(5)
            scores.append(50 * num)
            return (50 * num)
        if 1 in rolls:
            nums = rolls.count(1)
            scores.append(100 * nums)
            return(100 * nums)
        # elif len(rolls > 0):
        #return sum(scores)
        return sum(scores)
    