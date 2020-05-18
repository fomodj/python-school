import pickle
from classdeomo.cellphone import CellPhone

FILENAME = 'cellphone.data'

def main():
    end_of_file = False

    #Open the file
    input_file = open(FILENAME,'rb')

    #Read the file to the end of it
    while not end_of_file:
        # 反序列化 unpickle the next object
        try:
            phone = pickle.load(input_file)
            print(phone)
        except EOFError:
            end_of_file = True
            input_file.close()
main()