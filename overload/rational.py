class Rational:
    '''
    Rational number
    denominator 分母
    numeration 分子
    '''
    def __init__(self,numerator,denominator):
        self.__numeration = numerator
        self.__denominator = denominator
        self.__reduce = self.__reduce__()

    def get_denominator(self):
        return self.__denominator

    def set_denominator(self,denominator):
        if not isinstance(denominator,float) and not isinstance(denominator,int):
            print("必须是浮点型或者整型")
            return
        self.__denominator = denominator

    def get_numeration(self):
        return self.__numeration

    def set_numeration(self,numeration):
        self.__numeration = numeration

    def gcd(a,b):# 求a和b的最大公约数
        if a is b:
            return a
        elif a.__numeration == b.__numeration and \
                a.__denominator == b.__denominator:
            return a
        else:
            # 求分子最大公约数
            if a.__numeration > b.__numeration:
                smaller = b.__numeration
            else:
                smaller = a.__numeration
            for i in range(1, smaller + 1):
                if ((a.__numeration % i == 0) and (b.__numeration % i == 0)):
                    new_nu = i
            # 求分母最小公倍数
            if a.__denominator > b.__denominator:
                greater = a.__denominator
            else:
                greater = b.__denominator
            while (True):
                if ((greater % a.__denominator == 0) and (greater % b.__denominator == 0)):
                    new_de = greater
                    break
                greater += 1
        new_rational = Rational(new_nu, new_de)
        return new_rational

    def __reduce__(self):# 对有理数进行约分，最简分数
        for i in range(2, self.__denominator):
            while (self.__denominator % i == 0 and self.__numeration % i == 0):
                self.__denominator = self.__denominator // i
                self.__numeration = self.__numeration // i
        return self.__numeration,self.__denominator

    def __str__(self):
        return str(self.__numeration)+'/'+str(self.__denominator)

    '''
    __add__     +
    __sub__     -
    __mul__     *
    __div__     /
    __mod__     %
    
    == __eq__   != __ne__   < __lt__    <= __le__   > __gt__    >= __ge__
    '''

    def __add__(self, other): # 加法
        new_nu = self.__numeration * other.__denominator + self.__denominator * other.__numeration
        new_de = self.__denominator * other.__denominator
        new_rational = Rational(new_nu,new_de)
        return new_rational

    def __sub__(self, other):# 减法
        new_nu = self.__numeration * other.__denominator - self.__denominator * other.__numeration
        new_de = self.__denominator * other.__denominator
        new_rational = Rational(new_nu, new_de)
        return new_rational

    def __mul__(self, other):# 乘法
        new_nu = self.__numeration * other.__numeration
        new_de = self.__denominator * other.__denominator
        new_rational = Rational(new_nu, new_de)
        return new_rational

    def __truediv__(self, other):# 除法
        new_nu = self.__numeration * other.__denominator
        new_de = self.__denominator * other.__numeration
        new_rational = Rational(new_nu, new_de)
        return new_rational

    def __eq__(self, other):# 是否相等
        if self is other:
            return True
        elif type(self) != type(other):
            return False
        elif self.__numeration == other.__numeration and \
                self.__denominator == other.__denominator:
            return True
        else:
            return self.__numeration * other.__denominator == self.__denominator * other.__numeration

    def __lt__(self,other): # 小于
        if self.__numeration * other.__denominator < self.__denominator * other.__numeration:
            return True
        else:
            return False

    def __ne__(self, other): # 不等于
        if self.__numeration * other.__denominator != self.__denominator * other.__numeration:
            return True
        else:
            return False

