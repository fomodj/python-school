import pickle
from employee import Employee

FILENAME = 'employee.data'

def main():

    # 创建并打开文件
    output_file = open(FILENAME, 'wb')
    # 数据
    people01 = Employee('Susan Meyers', '47899', 'Accouting', 'Vice President')
    people02 = Employee('Mark John', '39119', 'IT', 'Programmer')
    people03 = Employee('Joy Rogers', '81774', 'Manufacturing', 'Engineer')
    # 序列化
    pickle.dump(people01,output_file)
    pickle.dump(people02,output_file)
    pickle.dump(people03,output_file)
    output_file.close()
    print("The data was written to" + FILENAME)
main()