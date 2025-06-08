from abc import ABC, abstractmethod
from logger import logger


class Vehicle(ABC):
    @abstractmethod
    def start_engine(self) -> None:
        pass


class VehicleFactory(ABC):

    @abstractmethod
    def create_car(self) -> Vehicle:
        pass

    @abstractmethod
    def create_motorcycle(self) -> Vehicle:
        pass


class USVehicleFactory(VehicleFactory):
    def create_car(self, make, model):
        return Car(make, model, "US Spec")

    def create_motorcycle(self, make, model):
        return Motorcycle(make, model, "US Spec")


class EUVehicleFactory(VehicleFactory):
    def create_car(self, make, model):
        return Car(make, model, "EU Spec")

    def create_motorcycle(self, make, model):
        return Motorcycle(make, model, "EU Spec")


class Car(Vehicle):
    def __init__(self, make, model, spec):
        self.make = make
        self.model = model
        self.spec = spec

    def start_engine(self):
        logger.info(f"{self.make} {self.model} {self.spec}: Двигун запущено")


class Motorcycle(Vehicle):
    def __init__(self, make, model, spec):
        self.make = make
        self.model = model
        self.spec = spec

    def start_engine(self):
        logger.info(f"{self.make} {self.model} {self.spec}: Мотор заведено")


us_factory = USVehicleFactory()
eu_factory = EUVehicleFactory()

vehicle1 = us_factory.create_car("Toyota", "Corolla")
vehicle1.start_engine()

vehicle2 = eu_factory.create_motorcycle("Harley-Davidson", "Sportster")
vehicle2.start_engine()
