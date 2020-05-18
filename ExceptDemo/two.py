try:
    filename = input("Enter a name of a file:")
    f = open(filename,'r')
    line = f.readline()
    num = int(line)
    print(num/0)
except FileNotFoundError as e:
    print("Error1: ",str(e))
except ValueError as e:
    print("Error2: ",str(e))
except:
    print("Other error")