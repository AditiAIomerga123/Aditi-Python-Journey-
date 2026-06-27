# 16va Practical: Functions - Calculator
print("🧮 Functions + Calculator")
print("="*35)

# Function banavle - reuse karayla soppe
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! 0 ne bhagta yet nahi"
    return a / b

# Main program
print("1. Add \n2. Subtract \n3. Multiply \n4. Divide")
choice = int(input("\nOption nivad 1-4: "))

num1 = float(input("Pahila number: "))
num2 = float(input("Dusra number: "))

# Function call karun result kadhla
if choice == 1:
    print(f"Result: {add(num1, num2)}")
elif choice == 2:
    print(f"Result: {subtract(num1, num2)}")
elif choice == 3:
    print(f"Result: {multiply(num1, num2)}")
elif choice == 4:
    print(f"Result: {divide(num1, num2)}")
else:
    print("Chukicha option!")

print("\nFunctions practical complete! 🎉")