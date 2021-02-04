import sys

#In function calculator(a, b, c):
#a, b - numbers
#c - choice
#choice 1 - add
#choice 2 - subtract
#choice 3 - multiply
#choice 4 - divide

#To compile and run: python3 calculator.py

def calculator(a, b, c):
    if (c == 1):
        if (not isinstance(a, int) and not isinstance(a, float)) or (not isinstance(b, int) and not isinstance(b, float)):
            print("Your input is invalid.")
            return None
        else:
            addition = a + b
            return addition
    if (c == 2):
        if (not isinstance(a, float) and not isinstance(a, int)) or (not isinstance(b, float) and not isinstance(b, int)):
            print("Your input is invalid.")
            return None
        else:
            subtraction = a - b
            return subtraction
    if (c == 3):
        if (not isinstance(a, float) and not isinstance(a, int)) or (not isinstance(b, float) and not isinstance(b, int)):
            print("Your input is invalid.")
            return None
        else:
            multiplication = a * b
            return multiplication
    if (c == 4):
        if (not isinstance(a, int) or not isinstance(b, int)):
            print("Your input is invalid.")
            return None
        elif (b == 0):
            print("Cannot divide by zero.")
            return None
        else:
            division = a / b
            return division
    else:
        print("Invalid choice.");
        return None


