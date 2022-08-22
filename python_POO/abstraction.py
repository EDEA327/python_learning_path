class Washing_machine:
    def __init__(self):
        pass
    def washing(self,temp = "hot"):
        self._fill_water_tank(temp)
        self._add_soap()
        self._wash()
        self._spin_dry()
    def _fill_water_tank(self,temp):
        print(f'Filling tank with {temp} water ')
    def _add_soap(self):
        print(f'Adding SOAP')
    def _wash(self):
        print(f'Washing clothes')
    def _spin_dry(self):
        print(f'Spinning dry clothes')

if __name__ == '__main__':
    washer = Washing_machine()
    washer.washing()


