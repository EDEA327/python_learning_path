import time
from typing import Generator
def fibo_gen(n_max:int ) -> Generator:
    """Generates a fibonacci sucesion until n_max is reached"""
    # Se declaran las variables iniciales de la sucesion de fibonacci
    n1:int = 0
    n2:int = 1
    # Si no ha llegado al maximo o si el maximo es mayor o igual que n1 el ciclo se ejecuta
    while not n_max or n_max >= n1:
        # Retenemos el valor de n1 para que la funcion sea más rapida
        # en el primer ciclo es 0
        # en el segudo ciclo es 1
        # en el tercero es 0 +1 y asi para todos los demás iteraciones
        yield n1
        # intercambiamos los valores en la sucesion
        n1, n2 = n2, n1 + n2

if __name__ == '__main__':
    # Creamos el objeto y le enviamos un numero maximo u_num
    #! La sucesion se detendra antes de llegar a 10 si queremos que se impriman 10 sucesiones debemos usar un ciclo for en fibo_gen
    u_num:int = int(input("Please type a number to generate fibonacci sucesion: "))
    assert u_num > 0,"Only positive numbers are allowed"
    fibonacci: Generator = fibo_gen(u_num)
    for element in fibonacci:
        print(element)
        time.sleep(.5)