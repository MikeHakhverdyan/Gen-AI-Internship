from typing import Literal


# from main import deleter

class Resource:

    '''
    Main Class from which the other Classes going to Inherit
    '''

    def __init__(self,
                 item_type: Literal['CPU', 'SSD', 'HDD'],
                 manufacturer: str,
                 model: str,
                 ):

        self._item_type = item_type
        self.manufacturer = manufacturer
        self.model = model

    @property
    def item_type(self):
        return self._item_type

    @property
    def model(self):
        return self._model

    @property
    def manufacturer(self):
        return self._manufacturer

    @property
    def state(self):
        return self._state


    '''
    Functions for Moving a Device from One place to Another
    '''

    def allocate(self):
        if self._state == 'Allocated':
            print('The Device is already Allocated')
            return
        elif self._state == 'Retired':
            print("The Device is retired and can't be Used Anymore")
            return
        elif self.assocation_to_trackers[self._state][self._item_type][self._manufacturer][self._model] >= 1:
            self.assocation_to_trackers[self._state][self._item_type][self._manufacturer][self._model] -= 1
            self._state = 'Allocated'
            try:
                self.assocation_to_trackers[self._state][self._item_type][self._manufacturer][self._model] += 1
            except KeyError:
                self.assocation_to_trackers[self._state][self._item_type][self._manufacturer][self._model] = 1
            print('The Device is Succesfully Allocated!')


    def to_inventory(self):
        if self._state == 'Inventory':
            print('The Device is already in Inventory')
            return
        elif self._state == 'Retired':
            print("The Device is retired and can't be Used Anymore")
            return
        elif self.assocation_to_trackers[self._state][self._item_type][self._manufacturer][self._model] >= 1:
            self.assocation_to_trackers[self._state][self._item_type][self._manufacturer][self._model] -= 1
            self._state = 'Inventory'
            try:
                self.assocation_to_trackers[self._state][self._item_type][self._manufacturer][self._model] += 1
            except KeyError:
                self.assocation_to_trackers[self._state][self._item_type][self._manufacturer][self._model] = 1
            print('The Device is Moved to Inventory')

    def retire(self):
        if self._state == 'Retired':
            print('The Device is already Retired')
            return
        elif self.assocation_to_trackers[self._state][self._item_type][self._manufacturer][self._model] >= 1:
            self.assocation_to_trackers[self._state][self._item_type][self._manufacturer][self._model] -= 1
            self._state = 'Retired'
            try:
                self.assocation_to_trackers[self._state][self._item_type][self._manufacturer][self._model] += 1
            except KeyError:
                self.assocation_to_trackers[self._state][self._item_type][self._manufacturer][self._model] = 1
            print('The Device is Retired and Have no Access Anymore(((')
            self.deleter()



    '''
    Trackers
    '''

    total_tracker = {
        'CPU': {'Intel': {}, 'AMD': {}},
        'HDD': {},
        'SSD': {}
    }

    inventory_tracker = {
        'CPU': {'Intel': {}, 'AMD': {}},
        'HDD': {},
        'SSD': {}
    }

    allocated_tracker = {
        'CPU': {'Intel': {}, 'AMD': {}},
        'HDD': {},
        'SSD': {}
    }

    retired_tracker = {
        'CPU': {'Intel': {}, 'AMD': {}},
        'HDD': {},
        'SSD': {}
    }

    assocation_to_trackers = {
        'Inventory': inventory_tracker,
        'Allocated': allocated_tracker,
        'Retired': retired_tracker
    }
