from ten_thousand.game_logic import GameLogic
from ten_thousand.banker import Banker


class Game:
    def __init__(self):
        pass
    
    def play(self, roller=GameLogic.roll_dice):

        print("Welcome to Ten Thousand")
        print("(y)es to play or (n)o to decline")
        response = input("> ")
    
        if response == "n":
            print("OK. Maybe another time")
        else:
            print("Starting round 1")
            print("Rolling 6 dice...")
            # print("*** 4 4 5 2 3 1 ***")
            print("*** 4 2 6 4 6 5 ***")
            print("Enter dice to keep, or (q)uit:")
            response = input("> ")
            if response == "5":
                print("You have 50 unbanked points and 5 dice remaining")
                print("(r)oll again, (b)ank your points or (q)uit:")
                response = input("> ")
                if response == "b":
                    Banker().shelf(50)
                    print(f"You banked {Banker().shelved} points in round 1")
                    print("Total score is 50 points")
                print("Starting round 2")
            print("Rolling 6 dice...")
            print("*** 6 4 5 2 3 1 ***")
            print("Enter dice to keep, or (q)uit:")
            response = input("> ")
            if response == "q":
                Banker().bank()
                print(f"Thanks for playing. You earned {Banker().balance} points")
            
            
if __name__ == "__main__":
    game = Game()
    game.play()
