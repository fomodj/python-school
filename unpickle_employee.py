import pickle
from employee import Employee
FILENAME = 'employee.data'
def main():
    end_of_file = False
    # 打开文件
    input_file = open(FILENAME,'rb')
    # 一直读取到文件的最后
    while not end_of_file:
        try:
            # 反序列化并转成字典
            people01 = pickle.load(input_file).__dict__
            people02 = pickle.load(input_file).__dict__
            people03 = pickle.load(input_file).__dict__
            print(people01)
            print(people02)
            print(people03)
            # 所有信息放入一个列表
            list = [people01,people02,people03]
            print(list)
        except EOFError:
            end_of_file = True
            input_file.close()
main()