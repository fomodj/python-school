# import numpy as np
#
# # 使用random模块来随机生成2000个0,1的值（掷硬币值）（两个结果任选一个），利用函数使0变成-1
# vector = np.random.choice([0,1],20)
# equal_to_zero = (vector==0)
# vector[equal_to_zero] = -1
#
# # 使用cumsum()函数步数累计和，显示酒鬼每一步距原点的距离
# cum_sum1 = vector.cumsum()*0.5
# print('酒鬼每一步距原点的距离(米):\n',cum_sum1)
#
# cum_sum = vector.cumsum()
# print('酒鬼每一步距原点的距离(米):\n',cum_sum*0.5)
