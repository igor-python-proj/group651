# родительский класс, суперкласс
class Car:
    # конструктор, инициализатор
    def __init__(self, color, horse_power):
        self.color = color
        self.horse_power = horse_power

    def drive_to(self, destination):
        print(f"Car {self.color} driving to {destination}")

    def change_color(self, new_color):
        self.color = new_color

# дочерний класс, класс-наследник, подкласс
class Bus(Car):
    def __init__(self, color, horse_power, number_seats):
        super().__init__(color, horse_power)
        self.number_seats = number_seats

    def drive_to(self, destination):
        # super().drive_to(destination)
        print(f"Bus {self.color} driving to {destination}")

    def test(self):
        print(f"test {self.color}")

class Truck(Car):
    def change_color(self, new_color):
        self.color = new_color
        print(f"Цвет грузовика поменялся на {self.color}")


bus_38 = Bus(horse_power=200, number_seats=40, color="green")
bus_38.drive_to("Bishkek")
print(bus_38.color)
print(type(bus_38))
print("Bus object is a bus: ", isinstance(bus_38, Bus))
print("Bus object is a car: ", isinstance(bus_38, Car))
car_1 = Car("silver", 1000)
truck_1 = Truck("red", 400)

vehicles = [car_1, truck_1, bus_38]
for v in vehicles:
    v.drive_to(destination="Karakol")