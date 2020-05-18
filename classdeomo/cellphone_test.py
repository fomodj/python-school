import classdeomo.cellphone as c

def main():
    man = input("Enter manufacturer:")
    model = input("Enter the model number:")
    price = float(input("Enter the retail price:"))

    phone = c.CellPhone(man,model,price)
    # print("Manufacturer:",phone.get_manufact())
    # print("Model Number:",phone.get_model())
    # print("Retail Price:",phone.get_price())
    print(phone.__str__())
main()