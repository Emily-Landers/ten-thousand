from collections import Counter
import random


class GameLogic:
    @staticmethod     
    def roll_dice(num=6):
        rolls = [random.randint(1, 6) for _ in range(num)]
        return tuple(rolls)

    @staticmethod
    def calculate_score(dice):

        if len(dice) > 6:
            raise Exception("no, its not a pomegranate")

        counts = Counter(dice)

        if len(counts) == 6:
            return 1500

        if len(counts) == 3 and all(val == 2 for val in counts.values()):
            return 1500

        score = 0

        ones_used = fives_used = False

        for num in range(1, 6 + 1):

            pip_count = counts[num]

            if pip_count >= 3:

                if num == 1:

                    ones_used = True

                elif num == 5:

                    fives_used = True

                score += num * 100

                pips_beyond_3 = pip_count - 3

                score += score * pips_beyond_3
                
                if num == 1:
                    score *= 10

        if not ones_used:
            score += counts.get(1, 0) * 100

        if not fives_used:
            score += counts.get(5, 0) * 50

        return score
        
@staticmethod
def scorers(dice):
        all_dice = GameLogic.calculate_score(dice)
            
        if all_dice == 0:
                return tuple()
            
        scorers = []
        
        for i, val in enumerate(dice):
            sub_roll = dice[:i] + dice[i + 1 :]
            sub_score = GameLogic.calculate_score(sub_roll)

            if sub_score !=             all_dice:
                scorers.append(val)

        return tuple(scorers)
            
            