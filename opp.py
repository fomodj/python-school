import math
def getarea(radius):
    return math.pi*radius*radius
def getparimeter(radius):
    return 2*math.pi*radius

if __name__=='__main__':
    radius = 28
    print("半径为%10.2f的圆的面积为%10.2f"%(radius,getarea(radius)))
    print("半径为{}的圆的周长是{}".format(radius,getparimeter(radius)))