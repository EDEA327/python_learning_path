def run():
    option = 'Y'
    count = 0
    while option == 'Y' :
        if count == 0:
            num = int(input('What number do you want to know the multiplication tables for? '))
            tables(num)
            option = str(input('Do you want to do the multiplication tables for another number? [Y/n]: ' + "\n"))
        else:
            num = int(input('Write the new number: '))
            tables(num)
            option = str(input('Do you want to continue? [Y/n]: ' + "\n"))
        while option != 'Y' and option != 'n':
            print('Please enter a valid option \n')
            option = str(input('Do you want to continue? [Y/n]: '))
        count += 1
def tables(num):
    for i in range(1,11):
        print (str(num)+' X '+ str(i) + ' = ' + str(i*num))


if __name__ == '__main__':
    run()