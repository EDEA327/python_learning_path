# import sys
# sys.path.append("./operators.py")
from operators import *

def run():
    menu= """
    1-Addition
    2-Subtraction
    3-Multiplication
    4-Division
    Plese select an option:  """

    try:
        option = int(input(menu))
        num1 = input("Type your first number: ")
        assert num1.isnumeric()
        num2 = input("Type your second number: ")
        assert num2.isnumeric()
    # Para evitar problemas con las operaciones puse tipo float para hacerlo más general
        num1 = float(num1)
        num2 = float(num2)
    # Ejececucion según lo escogido
        if option == 1:
            print(f"{num1} + {num2} = {addition(num1,num2)}")
        elif option == 2:
            print(f"{num1} - {num2}  = {subtraction(num1,num2)}")
        elif option == 3:
            print(f"{num1} * {num2} ={multiplication(num1,num2)}")
        elif option == 4:
            print(f"{num1} / {num2} {division(num1,num2)}")
    except ValueError:
        print("Type a valid option number")

if __name__ == '__main__':
    run()
