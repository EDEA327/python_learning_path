# import sys
# sys.path.append("./operators.py")
from operators import *

def run():
    menu= """
    Plese select an option
    1-Addition
    2-Subtraction
    3-Multiplication
    4-Division
    """
    option = int(input(menu))
    num1 = input("Type your first number: ")
    assert num1.isnumeric,"must be a number"
    num2 = input("Type your second number: ")
    assert num2.isnumeric,"must be a number"
    if option == 1:
        print(f" The addition  is {addition(num1,num2)}")
    elif option == 2:
        print(f"The subtraction is {subtraction(num1,num2)}")
    elif option == 3:
        print(f"The multiplication is {multiplication(num1,num2)}")
    elif option == 4:
        print(f"The division is {division(num1,num2)}")

if __name__ == '__main__':
    run()
