import math
class Circle:
    __number = 0 # 类属性，定义在 类内部，方法的外部
    def __init__(self,radius):
        self._radius = radius # 实例属性
        Circle.__number += 1

    @classmethod # 类方法
    def get_number_class(cls):
        return cls.__number

    @staticmethod # 静态方法
    def get_number_static():
        return Circle.__number
    # 以上为两种方法

    def get_radius(self): #获取属性值 访问器 Accessor getter
        return self._radius
    def set_radius(self,r): #修改属性值 赋值器/修改器 Mutator setter
        if r < 0:
            print(str(r)+"不能为负值")
            return
        else:
            self._radius = r

    def getArea(self):
        return math.pi * self._radius * self._radius

if __name__ == '__main__':
    # c = Circle(2.0)
    # print(c.get_radius())
    # c.set_radius(4)
    # print(c.getArea())
    # c.set_radius(-4)
    # print(c.getArea())

    alist = []
    for i in range(10):
        alist.append(Circle(2))
    print(Circle.get_number_class())
    print(Circle.get_number_static())