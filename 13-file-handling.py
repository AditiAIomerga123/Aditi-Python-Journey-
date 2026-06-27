# 13va Practical: File Handling - Shivaji College
print("📝 File Handling Practical")
print("="*35)

# Step 1: User kadun data ghe
name = input("Tujha nav tak: ")
marks = input("SSC madhe kiti marks? ")

# Step 2: File madhe lihine - 'w' mode
file = open("student_data.txt", "w")
file.write(f"Student Name: {name}\n")
file.write(f"SSC Marks: {marks}\n")
file.write("College: Shivaji College, Miraj\n")
file.close()
print("\n✅ Data student_data.txt madhe save zala!")

# Step 3: File madhun vachne - 'r' mode  
print("\n📖 File madhun data vachuya:")
file = open("student_data.txt", "r")
print(file.read())
file.close()

print("\nFile handling complete! 🎉")