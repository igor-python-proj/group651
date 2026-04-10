class Animal:
    def move(self):
        print("Животное двигается")


class Swimming(Animal):
    def move(self):
        super().move()
        print("плавает")


class Flying(Animal):
    def move(self):
        super().move()
        print("летает")


class Duck(Flying, Swimming):
    def move(self):
        super().move()
        print("утка плавает и летает")


duck = Duck()
duck.move()
# method resolution order
print(Duck.__mro__)
