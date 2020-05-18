class CellPhone:
    def __init__(self,manufact,model,price):
        self.__manufact = manufact
        self.__model = model
        self.__price = price
    def get_manufact(self):
        return self.__manufact
    def set_manufact(self,man):
        self.__manufact = man
    def get_model(self):
        return self.__model
    def set_model(self,model):
        self.__model = model
    def get_price(self):
        return self.__price
    def set_price(self,price):
        self.__price = price

    def __str__(self):#描述对象信息
        return "Manufacturer:{}\nModel:{}\nPrice:{}".format(self.__manufact,self.__model,self.__price)

