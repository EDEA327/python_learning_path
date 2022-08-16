def validation(option):
    if option == 1:
            num = int(input('Type a number to know if it is a prime: '))
            if prime(num):
                print('Prime number')
            else:
                print('No prime number')
    elif option == 2:
            n=int(input("Enter the number of first-prime numbers you want: "))
            get_first_n_primes(n)


def prime(numbers):
    if numbers == 1:
        return False
    else:
        counter = 0
    for i in range(1,numbers+1):
        if i == 1 or i == numbers:
            continue
        elif numbers % i == 0:
            counter += 1
    if counter == 0:
        return True
    else:
        return False


def get_first_n_primes(n):
    n_prime=[2]
    prime_counter = 1
    number = 3
    # Lo intenté pero no se porque no da 2 si ustedes saben arreglenlo por favor
    while prime_counter < n:
        for i in range (2,number):
            if number % i == 0:
                break
            elif i == number-1:
                #print(number)
                n_prime.append(number)
                prime_counter += 1
        number += 1
    print("The " + str(n) + " first prime numbers are\n" + str(n_prime))


def run():
    menu=""" What do you want to do?
    1- Know if a number is prime
    2- Know the first n prime numbers
    Please choose an option
    """
    choice = 'Y'
    while  choice == 'Y':
        option = int(input(menu))
        validation(option)
        while option != 1 and option != 2:
            option=int(input('Please enter a valid option (1 or 2) '))
            validation(option)
        choice=str(input('Please type Y to repeat or any key to finish: '))


if __name__ == '__main__':
    run()