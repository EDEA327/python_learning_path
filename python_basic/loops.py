
def run():
    LIMIT = int(input('Type your limit number: '))
    num = float(input('Type your number: '))
    counter = 0
    power_of_num = num**counter
    while power_of_num <= LIMIT:
        print( str(int(num)) +' raised to '  + str(counter) + ' is equal to ' + str(int(power_of_num)))
        counter += 1
        power_of_num = num**counter


if __name__ == '__main__':
    run()
