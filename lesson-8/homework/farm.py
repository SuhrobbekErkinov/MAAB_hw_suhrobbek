class Animal:
    def __init__(self, name, kind, color, sound):
        self.name = name
        self.kind = kind
        self.color = color
        self.sound = sound

    def walk(self):
        print(f"{self.name} is walking.")

    def run(self):
        print(f"{self.name} is running.")

    def jump(self):
        print(f"{self.name} is jumping.")

    def make_sound(self):
        print(f"{self.name} the {self.kind} says {self.sound}.")

    def __str__(self):
        return f"Animal(name={self.name}, kind={self.kind}, color={self.color}, sound={self.sound})"

class Cow(Animal):
    def __init__(self, name, color):
        super().__init__(name, "Cow", color, "moo")

    @staticmethod
    def make_milk():
        print("Cow is making milk.")

class Dog(Animal):
    def __init__(self, name, color):
        super().__init__(name, "Dog", color, "woo")

    @staticmethod
    def bark():
        print("Dog is barking.")

class Chicken(Animal):
    def __init__(self, name, color):
        super().__init__(name, "Chicken", color, "chip")

    @staticmethod
    def lay_eggs():
        print("Chicken is laying eggs.")

if __name__ == "__main__":
    cow = Cow("Annie", "brown")
    dog = Dog("Doggie", "black")
    chicken = Chicken("Chickie", "yellow")

    animals = [cow, dog, chicken]
    for animal in animals:
        print(animal)
        animal.walk()
        animal.run()
        animal.jump()
        animal.make_sound()
        print("")

    cow.make_milk()
    dog.bark()
    chicken.lay_eggs()