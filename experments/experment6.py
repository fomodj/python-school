import numpy as np

# 使用random模块来随机生成2000个0,1的值（掷硬币值）（两个结果任选一个），利用函数使0变成-1
vector = np.random.choice([0,1],2000)
equal_to_zero = (vector==0)
vector[equal_to_zero] = -1

# 使用cumsum()函数步数累计和，显示酒鬼每一步距原点的距离
cum_sum = vector.cumsum()*0.5
print('酒鬼每一步距原点的距离(米):\n',cum_sum)

# 找出酒鬼离原点正向最远、反向最远距离
print('酒鬼距离原点正向最远的距离：{}米'.format(cum_sum[cum_sum.argmax()]))
print('酒鬼距离原点反向最远的距离：{}米'.format(cum_sum[cum_sum.argmin()]))

# 当酒鬼距原点的距离大于或等于15米时，总共走了多少步？如果没有走到15米，请输出：'酒鬼最远也没走到15米'
count = 0
if all(abs(i) < 15 for i in cum_sum):
    print('酒鬼最远也没走到15米')
else:
    for i in cum_sum:
        count += 1
        if i == 15 or i == -15:
            break
    print('首次大于或等于15米时，所走的步数：',count)