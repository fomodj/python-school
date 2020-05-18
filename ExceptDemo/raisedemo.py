def division():
    apple = eval(input("Please enter the number of apples:"))
    children = eval(input("Please enter the number of kids:"))
    if apple<children:
        raise ValueError("苹果数不可小于孩子数！")
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
    except ValueError as e:
        print(e)

