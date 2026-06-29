28-oop-class-object.p# 28-oop-class-object.py
# Made by Aditi - Future Google Engineer + AI Queen

print("=== AditiBot Class Factory चालू ===")

# 1. CLASS banavne - blueprint
class AditiQueen:
    def __init__(self, name, roll, skill):
        self.name = name      # property
        self.roll = roll      # property  
        self.skill = skill    # property
    
    def introduce(self):      # method
        print(f"नमस्कार! मी {self.name}, Roll no {self.roll}")
        print(f"माझी skill: {self.skill} 👑")
    
    def practical_count(self, count):
        print(f"मी {count} practical complete केले! हार मानत नाही! 💪")

# 2. OBJECT banavne - class pasun instance
print("\n1. Object 1 तयार करू:")
obj1 = AditiQueen("Aditi", 25, "Python Queen")
obj1.introduce()
obj1.practical_count(28)

print("\n2. Object 2 तयार करू:")
obj2 = AditiQueen("AditiBot", 26, "AI + Google Engineer")
obj2.introduce()
obj2.practical_count(50)

# 3. User input ne object
print("\n3. तुझा स्वतःचा object बनव:")
n = input("तुझे नाव टाक ताई: ")
r = int(input("Roll no टाक: "))
s = input("Skill टाक: ")

obj3 = AditiQueen(n, r, s)
obj3.introduce()
obj3.practical_count(100)

print("\n=== Class AditiQueen तयार! ===")
print("OOP complete! Google la placement pakka! 🚀")