import random
class Coin:
    def __init__(self,side):
        self.side = side
    def toss(self): #抛硬币
        if random.randint(0,1)==0:
            self.side = 'Digit'
        else:
            self.side = 'Flower'
    def get_side(self):
        return self.side
