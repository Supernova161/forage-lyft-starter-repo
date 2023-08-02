class Engine:
    def __init__(self, fuel_consumption_rate):
        self.running = False
        self.fuel_consumption_rate = fuel_consumption_rate

    def start(self):
        if not self.running:
            self.running = True
            print("Engine started.")
        else:
            print("Engine is already running.")

    def stop(self):
        if self.running:
            self.running = False
            print("Engine stopped.")
        else:
            print("Engine is already stopped.")

    def is_running(self):
        return self.running

    def get_fuel_consumption_rate(self):
        return self.fuel_consumption_rate


class FuelTank:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current_level = capacity

    def refuel(self, amount):
        if amount > 0:
            self.current_level = min(self.current_level + amount, self.capacity)
            print(f"Refueled {amount} liters.")
        else:
            print("Invalid refueling amount. Please provide a positive value.")

    def get_fuel_level(self):
        return self.current_level

    def get_capacity(self):
        return self.capacity


class Transmission:
    def __init__(self):
        self.gear = 0

    def shift_up(self):
        if self.gear < 6:
            self.gear += 1
            print(f"Shifted up to gear {self.gear}.")
        else:
            print("Already in top gear.")

    def shift_down(self):
        if self.gear > 0:
            self.gear -= 1
            print(f"Shifted down to gear {self.gear}.")
        else:
            print("Already in neutral gear.")

    def get_gear(self):
        return self.gear


class Car:
    def __init__(self, make, model, year, fuel_tank_capacity, fuel_consumption_rate):
        self.make = make
        self.model = model
        self.year = year
        self.fuel_tank = FuelTank(fuel_tank_capacity)
        self.engine = Engine(fuel_consumption_rate)
        self.transmission = Transmission()
        self.speed = 0

    def start(self):
        if not self.engine.is_running():
            self.engine.start()
        else:
            print("Car is already running.")

    def stop(self):
        if self.engine.is_running():
            self.engine.stop()
            self.speed = 0
        else:
            print("Car is already stopped.")

    def accelerate(self, speed):
        if self.engine.is_running():
            self.speed = max(self.speed + speed, 0)
            print(f"Accelerating to {self.speed} km/h.")
        else:
            print("Cannot accelerate. Car engine is not running.")

    def brake(self):
        if self.speed > 0:
            self.speed = 0
            print("Car stopped.")
        else:
            print("Car is already stationary.")

    def get_make(self):
        return self.make

    def get_model(self):
        return self.model

    def get_year(self):
        return self.year

    def get_fuel_level(self):
        return self.fuel_tank.get_fuel_level()

    def is_engine_running(self):
        return self.engine.is_running()

    def get_speed(self):
        return self.speed


# Example usage
car1 = Car("Toyota", "Camry", 2022, fuel_tank_capacity=60, fuel_consumption_rate=8.5)
car1.start()
car1.accelerate(50)
print(f"Car details: {car1.get_make()} {car1.get_model()} ({car1.get_year()})")
print(f"Current speed: {car1.get_speed()} km/h")
car1.brake()
car1.stop()
