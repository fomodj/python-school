from inherit.person import Person
class Student(Person):
    def __init__(self,name,age,snumber):
        # super(Student,self).__init__(name,age)# 父类的继承
        Person.__init__(self,name,age) #父类继承的另一种写法
        self.__snumber = snumber
    def get_snumber(self):
        return self.__snumber
    def set_snumber(self):
        self.__snumber = snumber

    def __str__(self):
        return Person.__str__(self)+'\nsnumber:{}'.format(self.__snumber)

