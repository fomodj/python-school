def division():
    apple = eval(input("Please enter the number of apples:"))
    children = eval(input("Please enter the number of kids:"))
    assert apple>=children,"苹果数不可小于孩子数！"
    how = apple/children
    remain = apple%children
    if remain>0:
        print("{}个苹果平均分配给{}个小朋友，每人分到{}个，剩余{}个".format(apple,children,how,remain))
    else:
        print("{}个苹果平均分配给{}个小朋友，每人分到{}个".format(apple, children, how))

if __name__=='__main__':
    try:
        division()
    except ZeroDivisionError:
        print("人数不能为0")
    except AssertionError as e:
        print(e)

# assert 等价于带条件的raise语句
# assert 表达式 reason
# 表达式为真，什么都不做
# 表达式为假，抛出一个AssertionError
