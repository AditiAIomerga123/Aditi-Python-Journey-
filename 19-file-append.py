# 19va Practical: File Append - Data add karne
print("📝 File Append Practical")
print("="*35)

# Step 1: Nava students add karuya 'a' mode ne
print("Navin student cha data add karuya:")
nav = input("Student nav: ")
marks = input("Marks: ")

# 'a' = append mode. Jun data delete hot nahi, khali add hoto
file = open("student_data.txt", "a") 
file.write(f"{nav} : {marks} marks\n")
file.close()
print("\n✅ Data file madhe add zala!")

# Step 2: Sagla file vachuya
print("\n📖 Ata sagla database baghuya:")
file = open("student_data.txt", "r")
data = file.read()
print(data)
file.close()

print("Total lines:", len(data.split('\n'))-1)
print("\nFile Append practical complete! 🎉")