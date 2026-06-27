# 17va Practical: Factorial using Function
print("🔢 Factorial Calculator")
print("="*30)

# Function - recursive style, teacher la awadto
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1) # swatachya function la call

num = int(input("Konta number cha factorial pahije? "))

if num < 0:
    print("Error! Negative number cha factorial nahi")
else:
    result = factorial(num)
    print(f"\n{num}! = {result}")

print("\nFactorial practical complete! 🎉")