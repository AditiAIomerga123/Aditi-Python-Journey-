# 22va Practical: OOP - Class & Object
print("🏫 Class & Object Practical")
print("="*35)

# Class banavli - blueprint sarkhi
class Student:
    # Constructor - object banavtana chalto
    def __init__(self, nav, roll, marks):
        self.nav = nav      # attribute
        self.roll = roll
        self.marks = marks
    
    # Method - function class madhe
    def display(self):
        print(f"\nNav: {self.nav}")
        print(f"Roll No: {self.roll}")
        print(f"Marks: {self.marks}")
    
    def result(self):
        if self.marks >= 35:
            return "PASS ✅"
        else:
            return "FAIL ❌"

# Object banavle - class pasun
print("Pahila student:")
s1 = Student("Aditi", 101, 88)
s1.display()
print("Result:", s1.result())

print("\n" + "="*35)
print("Dusra student:")
n = input("Nav tak: ")
r = int(input("Roll tak: "))
m = int(input("Marks tak: "))

s2 = Student(n, r, m)
s2.display()
print("Result:", s2.result())

print("\nClass & Object practical complete! 🎉")