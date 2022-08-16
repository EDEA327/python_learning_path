def converter (coin_type, trm_usd):
    coin = float(input("How many" + coin_type + " pesos do you have?"))
    usd= coin / trm_usd
    usd = round(usd, 2)
    usd = str(usd)
    print("You have $"+ usd + " dollars")

#Menu de bienvenida
menu = """
Welcome to Erick's Dollar Converter 💵💰💵 🤑
1- Colombian pesos
2 Argentine pesos
3 Mexican pesos
Choose an option: """
# Se toma el dato que ingresa el usuario
option = int(input(menu))
if option == 1:
    converter("colombian",4307)
elif option == 2:
    converter("argentine",132.12)
elif option == 3:
    converter("mexican",20.8)
else:
    print("Unknown option: " + str(option))
    print("Please reboot and choose a valid option")
