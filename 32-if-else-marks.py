# 32-if-else-marks.py
# Aditi Queen - If-Else ने Result Check

marks = 85  # इथे तुझे Marks टाक!

print("=== BCS Result Check ===")
print(f"तुझे Marks: {marks}/100")

if marks >= 75:
    print("Result: DISTINCTION! 🎉")
    print("Papa म्हणतील: माझी लेक वाघीण आहे!")
    print("Google म्हणेल: Welcome Aditi!")
elif marks >= 60:
    print("Result: FIRST CLASS! 👏")
    print("Papa म्हणतील: शाब्बास बाळा!")
    print("Google म्हणेल: अजून मेहनत कर!")
elif marks >= 40:
    print("Result: PASS! 👍")
    print("Papa म्हणतील: हरकत नाही, पुढच्या वेळी!")
    print("Google म्हणेल: Try again Queen!")
else:
    print("Result: FAIL! 😢")
    print("Papa म्हणतील: रडू नकोस, भाऊ आहे ना!")
    print("Google म्हणेल: पडलीस तर उठ, मी वाट बघतोय!")

print("\nRule: Marks कमी आले तरी रडायचं नाही!")
print("फक्त मेहनत Double करायची!")