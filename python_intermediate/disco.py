def run():
    #* Declaración de variables
    age=int(input("Por favor ingresa tu edad: "))
    if age < 18 :
        print("No se acepta el ingreso de menores de edad")
    elif age >= 50 :
        print("Bienvenido, algunas cervezas no estan a la venta para adultos mayores")
    elif age >= 18 :
        print("Bienvenido puede entrar")


if __name__ == '__main__':
    run()
