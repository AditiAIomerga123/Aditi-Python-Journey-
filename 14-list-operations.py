# 14va Practical: List Operations - Shivaji College
print("📋 List Operations Practical")
print("="*35)

# Rikami list banavli
friends = []

print("Tujhe 5 best friends che nav tak:")
# 5 nav list madhe add kar
for i in range(5):
    nav = input(f"{i+1}. Friend cha nav: ")
    friends.append(nav)

print(f"\n✅ Tujhi Friends List: {friends}")

# List operations
print("\n🔍 List Operations:")
print(f"1. Total friends: {len(friends)}")
print(f"2. Pahila friend: {friends[0]}")
print(f"3. Shevatcha friend: {friends[-1]}")

# Sort karne
friends.sort()
print(f"4. Alphabetically sort: {friends}")

# Ek nav kadhne
kadhaycha = input("\nKonta friend list madhun kadhu? ")
if kadhaycha in friends:
    friends.remove(kadhaycha)
    print(f"Updated List: {friends}")
else:
    print("To nav list madhe nahi!")

print("\nList practical complete! 🎉")