class Car:

    def __init__(self, model, brand, color):
        self.model = model
        self.brand = brand
        self.color = color
        self._status = 'resting'
        self._motor = Motor(cylinders=4)

    def speed_up(self, kind='slow'):
        if kind == 'fast':
            self._motor.inject_gasoline(10)
        else:
            self._motor.inject_gasoline(3)

        self._status = 'moving'


class Motor:

    def __init__(self, cylinders, kind='gasoline'):
        self.cylinders = cylinders
        self.kind = kind
        self._temperatura = 0
        self._gasoline_lvl = 15

    def inyecta_gasolina(self, gasoline):
        self.gasoline = gasoline
