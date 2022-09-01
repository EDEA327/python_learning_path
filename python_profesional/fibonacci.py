import time
class FiboIter():
    #! self hace referencia al objeto futuro que voy a crear con esta clase
    def __init__(self, max = None):
        self.max = max
    #! Se crea el metodo iter
    def __iter__(self):
        self.n1 = 0
        self.n2 = 1
        self.counter = 0
        return self
    #! Se crea el metodo next
    def __next__(self):
        if self.counter == 0:
            self.counter += 1
            return self.n1
        elif self.counter == 1:
            self.counter += 1
            return self.n2
    #! Si no existe maximo funciona como el ejemplo del profe y si existe iterammos hasta el máximo
        elif not self.max or self.n2 < self.max:
            self.aux = self.n1 + self.n2
            self.n1, self.n2 = self.n2, self.aux
            self.counter += 1
            return self.aux
    #! Si no se cumple nada de lo anterior elevamos un StopIteration
        else:
            raise StopIteration

if __name__ == '__main__':
    fibonacci = FiboIter(21)
    for element in fibonacci:
        print(element)
        time.sleep(0.5)