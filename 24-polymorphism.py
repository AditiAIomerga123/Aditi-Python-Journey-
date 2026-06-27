# 24va Practical: Polymorphism - OOP
print("🎭 Polymorphism Practical")
print("="*35)
print("Ekch nav, vegle vegle kaam!")

# Parent Class
class Animal:
    def sound(self):
        print("Animal awaj karte...")

# Child Classes - saglyancha sound() vegla
class Dog(Animal):
    def sound(self):
        print("🐕 Dog bhunkto: Bow!")

class Cat(Animal):
    def sound(self):
        print("🐱 Cat miav karte: Meow Meow!")

class Cow(Animal):
    def sound(self):
        print("🐄 Cow hambarte: Moo Moo!")

# Polymorphism - ekch function, vegle output
print("Animal chi list banavli:")
animals = [Dog(), Cat(), Cow()]

for animal in animals:
    animal.sound() # saglyancha sound() vegla chalto!

print("\n" + "="*35)
print("Hech ahe Polymorphism!")
print("Ekch method nav - sound()")
print("Pan pratyek object vegla output dete")

print("\nPolymorphism practical complete! 🎉")