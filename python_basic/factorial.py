n= int(input('Please enter an integer: '))
def factorial(n):
    '''
    This funciton calculates the factorial of n
    n int > 0
    returns n!
    '''
    if n == 1:
        return 1
    return n *  factorial(n - 1)
print(f'The factorial is {factorial(n)}')
