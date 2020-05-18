"""
    File:  validateStringInput.py
    Description:  Simple program to demonstrate how to validate
    user-input string is one of a set of strings.   
"""

def main():
    validStrings = ['a', 'b', 'c']
    userInput = input("Please enter a, b, or c only: ").lower()
    while userInput not in validStrings:
        userInput = input("Invalid entry only enter a, b, or c: ")

    print("The valid entry was '%s'" % (userInput))


main()
