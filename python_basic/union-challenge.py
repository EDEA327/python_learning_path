import time # lo use para personalizar un poco el programa 😁


def exhaustive_enumeration(number): # la funcion nos devuelve la raiz cuadrada y si el numero no tiene raiz cuadrada nos lo dice.
    answer = 0
    while answer**2 < number:
        answer += 1
    if answer**2 == number:
        print(f'The square root of  {number} is {answer}')
    else:
        print(f'{number} does not  have an exact square root please try with another method.')

def approximation(number): #la funcion recibe un numero como parametro y nos devuelve su raíz cuadrada si la encontró
    epsilon = 0.001
    step = epsilon**2
    answer = 0.0
    while abs(answer**2 - number) >= epsilon and answer <= number:
        answer += step
    if abs(answer**2 - number) >= epsilon:
        print(f'Square root of {number} not found, try with another method')
    else:
        print(f'The square root of {number} is  {answer}')

def binary_search(number): #la funcion recibe un numero como parametro y nos devuelve su raíz cuadrada.
    epsilon = 0.001
    low = 0.0
    high = max(1.0, number)
    answer = (high + low) / 2
    while abs(answer**2 - number) >= epsilon:
        if answer**2 < number:
            low = answer
        else:
            high = answer
        answer = (high + low) / 2
    print(f'The square root of {number} is {answer}')

def validation(option):
    #la funcion valida que lo que ingresa el usuario sea valido para el programa y así evitar errores.
    #si todo está bien llama la funcion correspondiente segun sea el caso
    if option == 1:
        target_num = int(input('Please enter a number to know its square root: '))
        approximation(target_num)
    elif option == 2:
        target_num = int(input('Please enter a number to know its square root: '))
        binary_search(target_num)
    elif option == 3:
        target_num = int(input('Please enter a number to know its square root: '))
        exhaustive_enumeration(target_num)

def run():
    print('Charging...')
    time.sleep(2)
    print('Welcome to the program to know square roots')
    menu= """
    What method do you want to use?
    1-Approximation
    2-Binary search
    3-Exhaustive enumeration
    Please choose and option:
    """
    choice = 'Y'
    # Por si el usuario quiere buscar la raíz de otro numero
    while  choice == 'Y' or choice == 'y': # por si les da flojera poner la mayuscula xD
    # Se le pide al usuario la opcion y se guarda en la variable option
        option = int(input(menu))
    # Se llama la funcíon para que determine si la opcion es valida
        validation(option)
    #Uso el siguiente while para que el programa pida no acepte una opcion que no sea valida.
        while option !=1 and option!=2 and option!= 3:
            option=int(input('Please enter a valid option (1,2 or 3): '))
    # En este caso la funcion validation lo que hace es llamar a approximation o a binary_search segun sea el caso
            validation(option)
    # Le preguntamos al usuario si quiere continuar
        choice=str(input('Please type Y to repeat or any key to finish: '))

if __name__ == '__main__':
    run()