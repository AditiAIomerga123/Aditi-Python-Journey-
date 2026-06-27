# 15va Practical: Dictionary - Student Marks System
print("📚 Student Marks Database")
print("="*35)

# Rikama dictionary banavla
students = {}

print("3 students che data tak:")
# 3 students add kar
for i in range(3):
    nav = input(f"\n{i+1}. Student cha nav: ")
    marks = int(input("Marks tak 0-100: "))
    students[nav] = marks # nav: marks asa store hoto

print(f"\n✅ Sagla Database: {students}")

# Dictionary operations
print("\n🔍 Search & Operations:")
shodh = input("Kutlya student che marks pahije? ")

if shodh in students:
    print(f"{shodh} che marks: {students[shodh]}")
else:
    print("To student database madhe nahi!")

# Saglyancha average
total = sum(students.values())
avg = total / len(students)
print(f"\n📊 Class Average: {avg:.2f}")

# Pass/Fail check
print("\nPass/Fail List:")
for nav, marks in students.items():
    if marks >= 35:
        print(f"{nav}: {marks} - Pass ✅")
    else:
        print(f"{nav}: {marks} - Fail ❌")

print("\nDictionary practical complete! 🎉")