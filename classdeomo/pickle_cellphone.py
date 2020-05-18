import pickle
from classdeomo.cellphone import CellPhone
# phone  pickle.dump(phone,flie)
# phone  pickle.load(file)

FILENAME = 'cellphone.data'

def main():
    again = 'y' # Control the loop

    # Open a file
    output_file = open(FILENAME,'wb')

    # Get the data
    while again.upper()=="Y":
        man = input("Enter manufacturer:")
        model = input("Enter the model number:")
        price = float(input("Enter the retail price:"))
        again = input("Enter more phone data? (y/n):")
    # Create a CellPhone object
    phone  = CellPhone(man,model,price)
    pickle.dump(phone,output_file)



    # Close File
    output_file.close()
    print("The data was written to"+FILENAME)

main()