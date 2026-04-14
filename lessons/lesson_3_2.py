from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def test(self):
        print("test in Animal")

class Dog(Animal):
    def make_sound(self):
        print("Гааав")

    def test(self):
        print("test in Dog")

class Cat(Animal):
    def make_sound(self):
        print("Мяу")

puppy = Dog()
print(puppy)
puppy.make_sound()