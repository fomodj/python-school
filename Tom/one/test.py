width = 100

import math
def sigmoid(x):
    return 1/(1+math.exp(-x))

if __name__ =='__main__':
    print(__name__)
    print('*'*30)
    print("Sigmoid(10)=",sigmoid(10))
    print(min(34,45))
    print('*'*30)