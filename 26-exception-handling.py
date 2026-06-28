# 26va Practical: Exception Handling
print("🛡️ Exception Handling Practical")
print("="*35)
print("Error aala tari program crash nahi honar!")

# 1. ZeroDivisionError handle karne
print("\n1. Division karu:")
a = int(input("Pahila number: "))
b = int(input("Dusra number: "))

try:
    result = a / b
    print(f"Result: {a}/{b} = {result}")
except ZeroDivisionError:
    print("❌ Error: Zero ne divide karu shakat nahi!")
except ValueError:
    print("❌ Error: Number tak, akshar nako!")

# 2. IndexError handle karne
print("\n2. List cha element kadhu:")
list1 = [10, 20, 30]
try:
    index = int(input("Konta index pahije 0-2 madhe: "))
    print(f"Element: {list1[index]}")
except IndexError:
    print("❌ Error: Itka motha index nahi list madhe!")

# 3. Finally - error aala tari chaltoch
print("\n3. Finally block:")
try:
    num = int(input("Ek number tak: "))
    print(f"Tujha number: {num}")
except:
    print("Kahi tari chukla")
finally:
    print("✅ Finally: Ha block nehmi chalto!")

print("\nException Handling practical complete! 🎉")
print("Note: try = try kar, except = error pakad, finally = nehmi kar")