class Person:
    def __init__(self,name,age):
        self.__name = name
        self.__age = age

    def set_name(self,name):
        self.__name = name
    def set_age(self, age):
        self.__age = age

    def get_name(self,name):
        return self.__name
    def get_age(self,age):
        return self.__age

    def __str__(self):
        return "name：{}\nage:{}".format(self.__name,self.__age)
