# 25va Practical: Lambda + Map - Short code, motha kaam
print("⚡ Lambda + Map Practical")
print("="*35)

# Normal list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Original list:", numbers)

# 1. LAMBDA - nav nahi, ekach line function
# lambda input : output
square = lambda x: x * x
print(f"\nLambda test: 5 cha square = {square(5)}")

# 2. MAP - pratyek item var function apply
squares = list(map(lambda x: x*x, numbers))
print("Squares list:", squares)

# 3. MAP ne double kar
double = list(map(lambda x: x*2, numbers))
print("Double list:", double)

# 4. User input var map
print("\nTujhi list tak space ne separate:")
user_input = input()
user_list = list(map(int, user_input.split())) # string la int madhe convert

cubes = list(map(lambda x: x**3, user_list))
print("Tujhya number che cubes:", cubes)

print("\nLambda + Map practical complete! 🎉")
print("Note: Lambda = chota function, Map = loop cha shortcut!")