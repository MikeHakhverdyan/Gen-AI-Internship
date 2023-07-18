from Storage import Storage
from Tech_Guy_Project import Literal, Resource


class HDD(Storage):
    manufacturer_dict = {
        'Seagate': ['Barracuda', 'IronWolf', 'SkyHawk'],
        'Kingston': ['A400', 'UV500', 'KC600'],
        'Samsung': ['Spinpoint', 'T5 Portable', 'T7 Touch']
    }

    hdd_rpms = [5400, 5900, 7200, 10000, 15000]

    def __init__(self,
                 manufacturer: Literal['Seagate', 'Kingston', 'Samsung'],
                 model: str,
                 capacity_gb: Literal[128, 256, 512, 1024],
                 rpm: Literal[hdd_rpms]
                 ):

        super().__init__(manufacturer, model, capacity_gb)

        self.rpm = rpm
        self._state = 'Inventory'

        try:
            self.total_tracker['HDD'][self._manufacturer][self._model] += 1
            self.inventory_tracker['HDD'][self._manufacturer][self._model] += 1
        except KeyError:
            self.total_tracker['HDD'][self._manufacturer][self._model] = 1
            self.inventory_tracker['HDD'][self._manufacturer][self._model] = 1
            self.allocated_tracker['HDD'][self._manufacturer][self._model] = 0
            self.retired_tracker['HDD'][self._manufacturer][self._model] = 0

    def __str__(self):
        return f'{self._manufacturer} {self._model}'

    def __repr__(self):
        return f"{self._manufacturer} {self._model}\n" \
               f"Total: {self.total_tracker['HDD'][self._manufacturer][self._model]}\n" \
               f"Inventory: {self.inventory_tracker['HDD'][self._manufacturer][self._model]}\n" \
               f"Allocated: {self.allocated_tracker['HDD'][self._manufacturer][self._model]}\n" \
               f"Retired: {self.retired_tracker['HDD'][self._manufacturer][self._model]}"

    @property
    def rpm(self):
        return self._rpm

    @rpm.setter
    def rpm(self, speed):
        if speed in self.hdd_rpms:
            self._rom = speed
            return
        raise KeyError('Entered RPM is not Allowed')


hdd1 = HDD("Samsung", 'Spinpoint', 256, 7200)
print(hdd1)
print(repr(hdd1))
hdd1.allocate()
hdd1.to_inventory()
hdd1.retire()
hdd1.to_inventory()

print('inv ', Resource.inventory_tracker)
print('all ', Resource.allocated_tracker)
print('ret ', Resource.retired_tracker)
