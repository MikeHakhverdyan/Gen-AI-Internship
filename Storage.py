from Tech_Guy_Project import Resource
from Tech_Guy_Project import Literal


class Storage(Resource):
    def __init__(self,
                 manufacturer: str,
                 model: str,
                 capacity_gb: Literal[128, 256, 512, 1024]):
        super().__init__(self.__class__.__name__, manufacturer, model)
        self._capacity_gb = capacity_gb

    @property
    def capacity_gb(self):
        return self._capacity_gb

    @Resource.manufacturer.setter
    def manufacturer(self, manu):
        if manu in self.manufacturer_dict:
            self._manufacturer = manu
            return
        raise KeyError('Entered Manufacturer is not Allowed')

    @Resource.model.setter
    def model(self, new_name):
        if new_name in self.manufacturer_dict[self.manufacturer]:
            self._model = new_name
            return
        raise KeyError('Entered Model is not Allowed')
