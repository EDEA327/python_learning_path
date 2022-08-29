def is_prime(number: int) -> bool:
    """
    Check if the number is prime
    :param number:
    :return:
    """
    check_list = [i for i in range(2,number) if number % i == 0]
    return len(check_list) == 0

def run() -> None:
    """
    Main function
    """
    number: int = int(input('Number to check: '))
    if is_prime(number):
        print(f'{number} is prime')
    else:
        print(f'{number} is not prime')

if __name__ == '__main__':
    run()