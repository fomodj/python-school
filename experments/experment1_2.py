import random
list = []
s=''
for i in range(6):#控制长度，循环6次
    j = random.randint(0, 3)#分类随机三种情况
    if j == 1:
        n = random.randint(40,49)-40#40~49的随机数为数字0~9
        list.append(str(n))
    elif j == 2:
        n = random.randint(65,90)#65~90的随机数，转换为大写字母
        list.append(chr(n))
    else:
        n = random.randint(97,122)#97~122的随机数，转换为小写字母
        list.append(chr(n))
for i in list:
    s=s+i#转换为字符串输出
print(s)
