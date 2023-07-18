from Storage import Storage
from Tech_Guy_Project import Literal, Resource

class SSD(Storage):

    manufacturer_dict = {
        'Seagate': ['BarraCuda 510', 'FireCuda 520', 'IronWolf 510'],
        'Kingston': ['A2000', 'KC2500', 'KC2000'],
        'Samsung': ['970 EVO', '970 PRO', '980 PRO']
    }

    ssd_interfaces = [
        "PCIe NVMe 3.0 x4",
        "SATA III (6 Gbps)",
        "M.2 2280",
        "U.2 (SFF-8639)",
        "PCIe 4.0 x4",
    ]

    def __init__(self,
                 manufacturer: Literal['Seagate', 'Kingston', 'Samsung'],
                 model: str,
                 capacity_gb: Literal[128, 256, 512, 1024],
                 interface: str
                 ):

        super().__init__(manufacturer, model, capacity_gb)

        self.interface = interface
        self._state = 'Inventory'

        try:
            self.total_tracker['SSD'][self._manufacturer][self._model] += 1
            self.inventory_tracker['SSD'][self._manufacturer][self._model] += 1
        except KeyError:
            self.total_tracker['SSD'][self._manufacturer][self._model] = 1
            self.inventory_tracker['SSD'][self._manufacturer][self._model] = 1
            self.allocated_tracker['SSD'][self._manufacturer][self._model] = 0
            self.retired_tracker['SSD'][self._manufacturer][self._model] = 0

    def __str__(self):
        return f'{self._manufacturer} {self._model}'

    def __repr__(self):
        return f"{self._manufacturer} {self._model}\n" \
               f"Total: {self.total_tracker['SSD'][self._manufacturer][self._model]}\n" \
               f"Inventory: {self.inventory_tracker['SSD'][self._manufacturer][self._model]}\n" \
               f"Allocated: {self.allocated_tracker['SSD'][self._manufacturer][self._model]}\n" \
               f"Retired: {self.retired_tracker['SSD'][self._manufacturer][self._model]}"

    @property
    def interface(self):
        return self._interface

    @interface.setter
    def interface(self, name):
        if name in self.ssd_interfaces:
            self._interface = name
            return
        raise KeyError('Entered Interface is not Allowed')
