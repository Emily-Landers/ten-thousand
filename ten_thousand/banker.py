class Banker:
    
    def __init__(self):
        self.balance = 0
        self.shelved = 0
    
    def shelf(self, x):
        self.shelved += x
        
    def bank(self):
        deposit = self.shelved
        self.balance += self.shelved
        self.shelved = 0
        return deposit
        
    def clear_shelf(self):
        self.shelved = 0
        
    def check_balance(self):
        return self.balance    



