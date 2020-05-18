class Employee:
    def __init__(self,name,id,department,position):
        self.__name = name
        self.__id = id
        self.__department = department
        self.__position = position
    def __str__(self):
        return 'Name:'+self.__name+'\nId:'+self.__id+'\nDepartment:'+self.__department+\
            '\nPosition:'+self.__position


    # def getName(self):
    #     return self.__name
    # def setName(self,name):
    #     self.__name = name
    # def getId(self):
    #     return self.__id
    # def setId(self,id):
    #     self.__id = id
    # def getDepartment(self):
    #     return self.__department
    # def setDepartment(self,department):
    #     self.__department = department
    # def getPosition(self):
    #     return self.__position
    # def setPosition(self,position):
    #     self.__position = position