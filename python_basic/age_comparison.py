
def run():
    # asignacion de las variables
    name_1 = input("Type your name: ")
    age_1 = input("Age: ")
    name_2 = input("Type another name: ")
    age_2 = input("Age: ")

    if age_1 > age_2:
        print(f'{name_1} is older than {name_2}')
    elif age_1 < age_2:
        print(f'{name_1} is younger than {name_2}')
    else:
        print(f'{name_1} is the same age as {name_2}')

if __name__ == "__main__":
    run()