# 23va Practical: Inheritance - OOP
print("👨‍👩‍👧 Inheritance Practical")
print("="*35)

# Parent Class / Super Class
class Person:
    def __init__(self, nav, age):
        self.nav = nav
        self.age = age
    
    def display(self):
        print(f"Nav: {self.nav}")
        print(f"Age: {self.age}")

# Child Class / Sub Class - Person cha gun dharan karte
class Student(Person):
    def __init__(self, nav, age, roll, marks):
        super().__init__(nav, age) # Parent cha constructor call
        self.roll = roll
        self.marks = marks
    
    def display(self):
        super().display() # Parent cha method call
        print(f"Roll: {self.roll}")
        print(f"Marks: {self.marks}")
    
    def grade(self):
        if self.marks >= 75:
            return "Distinction 🎓"
        elif self.marks >= 60:
            return "First Class 🥇"
        else:
            return "Pass ✅"

# Object ban