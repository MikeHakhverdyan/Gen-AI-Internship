# if __name__ == '__main__':
from Tech_Guy_Project import Resource
from Tech_Guy_Project import Literal

class CPU(Resource):

    cpu_dict = {
    'AMD': (
        'Ryzen 9 5950X', 'Ryzen 7 5800X', 'Ryzen 5 5600X', 'Ryzen 9 5900X', 'Ryzen 7 5700X',
        'Ryzen 9 3900X', 'Ryzen 7 3800X', 'Ryzen 5 3600X', 'Ryzen 9 3950X', 'Ryzen 7 3700X',
        'Ryzen 5 3500X', 'Ryzen 9 3900XT', 'Ryzen 7 3800XT', 'Ryzen 5 3600XT', 'Ryzen 9 3950XT',
        'Ryzen 7 3700XT', 'Ryzen 5 3500XT', 'Ryzen 9 3900', 'Ryzen 7 3800', 'Ryzen 5 3600'
    ),
    'Intel': (
        'Core i9-11900K', 'Core i7-11700K', 'Core i5-11600K', 'Core i9-10900K', 'Core i7-10700K',
        'Core i5-10600K', 'Core i9-10850K', 'Core i7-10700KF', 'Core i5-10500K', 'Core i9-10980XE',
        'Core i7-10700', 'Core i5-10600', 'Core i3-10100', 'Core i9-10940X', 'Core i7-9700K',
        'Core i5-9600K', 'Core i9-10920X', 'Core i7-9700KF', 'Core i5-9600KF', 'Core i9-10900'
    )
    }

    def __init__(self,
                 manufacturer: Literal['AMD', 'Intel'],
                 model: str,
                 ):
        super().__init__('CPU', manufacturer, model)

        self._state = 'Inventory'

        try:
            self.total_tracker['CPU'][self._manufacturer][self._model] += 1
            self.inventory_tracker['CPU'][self._manufacturer][self._model] += 1
        except KeyError:
            self.total_tracker['CPU'][self._manufacturer][self._model] = 1
            self.inventory_tracker['CPU'][self._manufacturer][self._model] = 1
            self.allocated_tracker['CPU'][self._manufacturer][self._model] = 0
            self.retired_tracker['CPU'][self._manufacturer][self._model] = 0

    def __str__(self):
        return f'{self._manufacturer} {self._model}'

    def __repr__(self):
        return f"{self._manufacturer} {self._model}\n" \
               f"Total: {self.total_tracker['CPU'][self._manufacturer][self._model]}\n" \
               f"Inventory: {self.inventory_tracker['CPU'][self._manufacturer][self._model]}\n" \
               f"Allocated: {self.allocated_tracker['CPU'][self._manufacturer][self._model]}\n" \
               f"Retired: {self.retired_tracker['CPU'][self._manufacturer][self._model]}"

    @Resource.manufacturer.setter
    def manufacturer(self, manu):
        if manu in self.cpu_dict:
            self._manufacturer = manu
            return
        raise KeyError('Entered Manufacturer is not Allowed')

    @Resource.model.setter
    def model(self, new_name):
        if new_name in self.cpu_dict[self.manufacturer]:
            self._model = new_name
            return
        raise KeyError('Entered Model is not Allowed')
