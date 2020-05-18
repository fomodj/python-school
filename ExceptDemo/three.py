try:
    filename = input("Enter a name of a file:")
    f = open(filename,'r')
    line = f.readline()
    num = int(line)
    print(num/0)
except (FileNotFoundError,ValueError) as e:
    print("Error: ",str(e))
except:
    print("Other error")
finally:
    print("finally")
    f.close()