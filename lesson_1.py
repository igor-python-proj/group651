class Car:
    # конструктор, инициализатор
    def __init__(self, color, horse_power):
        self.color = color
        self.horse_power = horse_power

    def drive_to(self, destination):
        self.change_color("black")
        print(f"Car color {self.color} driving to {destination}")

    def change_color(self, new_color):
        self.color = new_color

car_1 = Car("silver", 1000)
car_2 = Car("black", 2500)
print(car_1)
print(car_1.color, car_2.color)
print(type(car_1))
car_1.drive_to("Karakol")
print(type("43243243"))
car_1.change_color("red")
print(car_1.color)
car_2.color = "red"
print(car_2.color)
car_2.model = "Subaru"
print(car_2.model)
# print(car_1.model)