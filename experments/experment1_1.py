import random
number = random.randint(1,100)
print("现在开始猜数游戏！（注意，你只有五次机会）")
for i in range(5):
    guess = int(input("请输入你猜的数字："))
    if guess > number:
        print("很遗憾，你猜大了")
    elif guess < number:
        print("很遗憾，你猜小了")
    else:
        print("恭喜，猜数成功")
        break
    print('剩余%d次猜数机会' %(6-i-2))
print("游戏结束，正确数字是%d"%number)
