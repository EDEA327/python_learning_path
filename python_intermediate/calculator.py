# import sys
# sys.path.append("./operators.py")
from operators import *

def run():
    menu= """
    1-Addition
    2-Subtraction
    3-Multiplication
    4-Division
    Type any key to Exit
    Plese select an option:  """
    foo = True
    options = (1, 2, 3, 4)
    while foo :
        try:
            option = int(input(menu))
            if option not in options:
                foo = False
                print("Bye bye!")
                break
            num1 = input("Type your first number: ")
            assert num1.isnumeric(),"Must be a number"
            num2 = input("Type your second number: ")
            assert num2.isnumeric(),"Must be a number"
        # Para evitar problemas con las operaciones puse tipo float para hacerlo más general
            num1 = float(num1)
            num2 = float(num2)
        # Ejececucion según lo escogido
            if option == 1:
                print(f"{num1} + {num2} =  {addition(num1,num2)}")
            elif option == 2:
                print(f"{num1} - {num2}  =  {subtraction(num1,num2)}")
            elif option == 3:
                print(f"{num1} * {num2} = {multiplication(num1,num2)}")
            elif option == 4:
                print(f"{num1} / {num2} = {division(num1,num2)}")
        except:
            break

if __name__ == '__main__':
    run()
