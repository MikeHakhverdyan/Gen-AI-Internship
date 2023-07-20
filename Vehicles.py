from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, tire :int, gear_shifting: str['Mechanical', 'Manual'], energy: 'Energy'):
        self.tire_count = tire
        self._energy = energy
        self._gear_shifting = gear_shifting

    @abstractmethod
    def braking(self):
        pass

    @abstractmethod
    def acceleration(self):
        pass

    @property
    def energy(self):
        return self._energy

    def add_energy(self, amount):
        self.energy.amount = amount

    @property
    def tyre_count(self):
        pass

    @tyre_count.setter
    def tyre_count(self, tire):
        pass

class Energy(ABC):
    def __init__(self, energy_type: str['Petrol', 'Gas', 'Muscle_Energy'], amount: int):
        self._energy = energy_type
        self._amount = amount

    @property
    def energy(self):
        return self._energy

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, amount):
        self._amount = amount


class Petrol(Energy):
    def __init__(self, amount):
        super().__init__("Petrol", amount)

class Gas(Energy):
    def __init__(self, amount):
        super().__init__("Gas", amount)


class Muscle_Energy(Energy):
    def __init__(self, amount):
        super().__init__("Muscle_Energy", amount)


class Car(Vehicle):
    def __init__(self, steering_wheel, tire, gear_shifting, energy):
        super().__init__(tire, gear_shifting, energy)
        self._steering_wheel = steering_wheel

    def braking(self):
        print("Stopping the car")

    def acceleration(self):
        print("Pedal to the Metal !!!")

    @property
    def tire_count(self):
        return self._tire

    @tire_count.setter
    def tire_count(self, tire):
        if tire != 4:
            raise ValueError("Car can have only 4 tires")
        self._tire = tire

class Bycicle(Vehicle):
    def __init__(self, tires, energy):
        super().__init__(tires, energy=energy, gear_shifting='Mechanical')

    def braking(self):
        print('Stopping the Bycicle')

    def acceleration(self):
        print('Pedalling as Hard as Possible !!!')

    @property
    def tire_count(self):
        return self._tire

    @tire_count.setter
    def tire_count(self, tire):
        if tire not in range(1, 4):
            raise ValueError("A Bicycle can have 1, 2 or 3 tires")
        self._tire = tire

    @property
    def gear_type(self, type):
        return self._gear_shifting

    @gear_type.setter
    def gear_type(self, type):
        if type != 'Mechanical':
            raise TypeError("A gear type for a bicycle can only be Mechanical")

class Motorcycle(Vehicle):

    def __init__(self, tires, gear_shifting, energy):
        super().__init__(tires, gear_shifting, energy)

    def acceleration(self):
            print('Vrooooommmm.... VROOOOOOOMMM')

    def braking(self):
            print('Stopping A Moto')

    @property
    def tire_count(self):
        return self._tire

    @tire_count.setter
    def tire_count(self, tire):
        if tire != 2:
            raise ValueError("A Motorcycle can have only 2 tires")
        self._tire = tire


