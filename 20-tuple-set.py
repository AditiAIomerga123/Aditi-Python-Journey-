# 20va Practical: Tuple & Set - Immutable data
print("🎯 Tuple & Set Practical")
print("="*35)

# 1. TUPLE - badalta yet nahi, immutable
print("1. TUPLE Example:")
college_info = ("Shivaji College", "Miraj", 1962, "Arts & Science")
print("College Tuple:", college_info)
print("College nav:", college_info[0])
print("Stapana varsha:", college_info[2])
print("Total items:", len(college_info))
# college_info[0] = "New College" # ERROR! Tuple badalta yet nahi

# 2. SET - duplicate nahi, order nahi
print("\n2. SET Example:")
subjects = {"Python", "DBMS", "OS", "Python", "Maths"} # Python 2da aahe
print("Subjects Set:", subjects) # Python ekdach disel
print("Total subjects:", len(subjects))

# Set operations
new_sub = input("\nNavin subject add kar: ")
subjects.add(new_sub)
print("Updated Set:", subjects)

# Membership check
check = input("DBMS aahe ka set madhe? ")
if check in subjects:
    print(f"Ho! {check} aahe ✅")
else:
    print(f"Nahi! {check} nahi ❌")

print("\nTuple & Set practical complete! 🎉")