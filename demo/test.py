import math
def sigmoid(x):
    return 1/(1+math.exp(-x))
def min(x,y):
    if x<y:
        return x
    else:
        return y
if __name__ =='__main__':
    print(__name__)
    print('*'*30)
    print("Sigmoid(10)=",sigmoid(10))
    print(min(34,45))
    print('*'*30)