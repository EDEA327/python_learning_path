class Washing_machine:
    def __init__(self):
        pass
    def lavar(self,temp = "Hot"):
        self._fill_water_tank(temp)
        self._add_soap()
        self._wash()
        self._spin_dry()
    def _fill_water_tank(self,temp):
        print(f'Filling tank with water {temp}')
    def _add_soap(self):
        print(f'Adding SOAP')
    def _wash(self):
        print(f'Washing')
    def _spin_dry(self):
        print(f'Spinning dry')

