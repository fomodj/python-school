try:
    for i in range(10):
        print(3/i)
except ZeroDivisionError as e:
    print("Error! "+str(e))