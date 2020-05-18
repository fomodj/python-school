# import test
# import matplotlib.pyplot as plt
# x = [i for i in range(-10,10)]
# y = [test.sigmoid(i) for i in x]
# plt.plot(x,y)
# plt.show()
# print(__name__)

from test import sigmoid
import matplotlib.pyplot as plt
x = [i for i in range(-10,10)]
y = [sigmoid(i) for i in x]
plt.plot(x,y)
plt.show()
print(__name__)