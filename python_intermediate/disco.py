def run():
    #* Declaración de variables
    age=int(input("Por favor ingresa tu edad: "))
    if age < 18 :
        print("No se acepta el ingreso de menores de edad")
    #! Si no le ponemos el menor de 50 nos puede pasar que ingresen un numero mayor de 50 y  se cumplirian las 2 condiciones
    #! de abajo.
    elif age >= 18 and age <= 50 :
        print("Bienvenido puede entrar")
    elif age > 50 :
        print("Bienvenido, algunas cervezas no estan a la venta para adultos mayores")

if __name__ == '__main__':
    run()
