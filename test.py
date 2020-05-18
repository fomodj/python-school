import math

class Rectangle:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def getarea(self):
        return self.x* self.y

    def getpairmeter(self):
        return 2*(self.x+self.y)
if __name__=="__main__":
    r1=Rectangular(3,4)
    print(r1. getarea())
    print(r1. getpairmeter())

