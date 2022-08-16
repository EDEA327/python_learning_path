def divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors


def run():
    try:
        num = int(input('Enter a number: '))
        if num < 0:
            raise ValueError("You can't enter a negative number") 
        print(divisors(num))
        print("Program finished.")
    except ValueError:
        print("You must enter a number")


if __name__ == '__main__':
    run()