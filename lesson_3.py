class Car:
    # конструктор, инициализатор
    def __init__(self, color, horse_power):
        self.color = color
        self.horse_power = horse_power
        self._fined = False
        self.__max_speed = 0

    def _calculate_fuel(self):
        print(f"{self.color}")
        print(self.__max_speed)
        return 1

    def __test(self):
        self.__max_speed = 180
        fined = "yes" if self._fined else "no"
        print(f"Car {self.color} is fined {fined}")

    def drive_to(self, destination):
        if self._calculate_fuel() > 0:
            self.change_color("green")
            print(f"Car {self.color} driving to {destination}")

    def change_color(self, new_color):
        self.color = new_color

    # геттер
    def get_max_speed(self):
        return self.__max_speed

    # сеттер
    def set_max_speed(self, new_speed):
        """Выставляет значение для приватного
        атрибута __max_speed"""
        print(f"new speed in set_max_speed: {new_speed}")
        if new_speed < 0:
            raise ValueError("Error, new speed cannot be negative")
        self.__max_speed = new_speed

    @property
    def max_speed(self):
        return self.__max_speed

    @max_speed.setter
    def max_speed(self, new_speed):
        print(f"new speed in max_speed: {new_speed}")
        if new_speed < 0:
            raise ValueError("Error, new speed cannot be negative")
        self.__max_speed = new_speed


car_1 = Car("silver", 1000)
print(car_1._fined)
car_1._calculate_fuel()
# car_1.__test()
# print(car_1.__max_speed)
# print(car_1._Car__max_speed)  # только для тестирования
# name mangling
print(car_1.get_max_speed())
car_1.__max_speed = 200 # не меняет настоящий атрибут
print(car_1.get_max_speed())
car_1.set_max_speed(200)
print(car_1.get_max_speed())
print(car_1.max_speed)
car_1.max_speed = -150
print(car_1.max_speed)
