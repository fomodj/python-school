from inherit.student import Student
from inherit.person import Person

#多态性
def printInfo(p):
    print(p)
    print('*'*30)

s = Student("Tom",20,"010")
printInfo(s)

p = Person('Jerry',21)
printInfo(p)

str1 = '123456'
printInfo(str1)

n = 10000
printInfo(n)