from ten_thousand.game_logic import GameLogic
from ten_thousand.banker import Banker
import sys

class Game:
    def __init__(self):
        self.banker = Banker()
        self.scorer = GameLogic()
        self.round_count = 0
        self.roller = None
        self.dice_count = 0
        self.keep_dice = []
        self.rolled_dice = None
    
    def play(self, roller=GameLogic.roll_dice):
        self.roller = roller
        print("Welcome to Ten Thousand")
        print("(y)es to play or (n)o to decline")
        response = input("> ")
    
        if response == "n":
            print("OK. Maybe another time")
            sys.exit()
        if response == "y":
        
            while True:
                self.dice_count = 6
                self.round_count += 1
                
                print(f"Starting round {self.round_count}")
                self.round_play()
                
    def round_play(self):
            print(f"Rolling {self.dice_count} dice...")
            self.rolled_dice = self.roller(self.dice_count)
            self.keep_()     
                       
    def keep_(self):
        roll_string = self.str_(self.rolled_dice)
        print(f"*** {roll_string} ***")
        if self.scorer.calculate_score(self.rolled_dice) == 0:
            self.zilch()
        print("Enter dice to keep, or (q)uit:")
        keep_ = input("> ").replace(" ", "")
        if keep_ == "q":
            print(f"Thanks for playing. You earned {self.banker.balance} points")
            sys.exit()
        else:
            self.keep_dice = []
            for j in keep_:
                self.keep_dice.append(int(j))
                
            self.check_cheater()

            self.dice_count -= len(self.keep_dice)
            self.banker.shelf(self.scorer.calculate_score(self.keep_dice))
            print(f"You have {self.banker.shelved} unbanked points and {self.dice_count} dice remaining")
            print('(r)oll again, (b)ank your points or (q)uit:') 
            r_b_q = input("> ")
            if r_b_q == "b":
                banked_points = self.banker.bank()
                print(f"You banked {banked_points} points in round {self.round_count}")
                print(f"Total score is {self.banker.balance} points")
            if r_b_q == "q":
                print(f"Thanks for playing. You earned  {self.banker.balance} points")
                sys.exit()

                       
    def str_(self, string):
        stringify = str(string)
        final = stringify.replace(",", "").replace("[","").replace("]", "").replace("(", "").replace(")", "")
        return final  
    def check_cheater(self):
        check_list = self.keep_dice
        check_rolled = [x for x in self.rolled_dice]

        for i in check_list:
            if i in check_rolled:
                check_rolled.remove(i)
            else:
                print("its a pomegranate")
                self.keep_()    
    def zilch(self):
        print("****************************************")
        print("**        Zilch!!! Round over         **")
        print("****************************************")
        
        print(f"You banked {self.banker.balance} points in round {self.round_count}")
        print(f"Total score is {self.banker.balance} points")
        
        self.dice_count = 6
        self.round_count += 1
        print(f"Starting round {self.round_count}")
        self.play_round()     
if __name__ == "__main__":
    game = Game()
    game.play()
