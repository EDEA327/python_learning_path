import time

def fibo_gen(n_max):
    n1, n2 = 0, 1
    while not n_max or n_max >= n1:
        yield n1
        n1, n2 = n2, n1 + n2

if __name__ == '__main__':
    fibonacci = fibo_gen(10)
    for element in fibonacci:
        print(element)
        time.sleep(.5)