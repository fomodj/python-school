# object oriented programming
import  math
class Circle:
    def __init__(self,radius):
        self.radius = radius
    def getarea(self):
        return self.radius * self.radius * math.pi
    def getparimeter(self):
        return 2 * self.radius * math.pi

if __name__=='__main__':
    c1 = Circle(30)
    print(c1.getarea())
    print(c1.getparimeter())

    print("半径为%10.2f的圆的面积为%10.2f" % (c1.radius, c1.getarea()))
    print("半径为{}的圆的周长是{}".format(c1.radius, c1.getparimeter()))