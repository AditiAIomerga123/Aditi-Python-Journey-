# 27-file-exception.py
# Made by Aditi - Future Google Engineer + AI Queen

print("=== AditiBot File Manager चालू ===")

filename = "aditi_queen.txt"

# 1. File write karne + exception
try:
    f = open(filename, "w")
    data = input("ताई file मध्ये काय लिहू? ")
    f.write(data)
    f.close()
    print(f"✅ '{filename}' file तयार झाली! AditiBot खुश!")
    
except Exception as e:
    print(f"❌ अरे error आला: {e} - AditiBot रडला!")

# 2. File read karne + exception
try:
    f = open(filename, "r")
    content = f.read()
    print(f"\n📖 File चा content: {content}")
    f.close()
    
except FileNotFoundError:
    print("❌ अरे ताई! File सापडली नाही! AditiBot हरवला!")
    
finally:
    print("✅ Finally: File बंद केली! Aditi हार मानत नाही! 💪")

# 3. Append karne - juna data safe
try:
    f = open(filename, "a")
    new_data = input("\nआजून काय add करू ताई? ")
    f.write("\n" + new_data)
    f.close()
    print("✅ Data add झाला! File आता अजून भारी झाली!")
    
except:
    print("❌ काहीतरी भलतंच झालंय!")

print("\n=== AditiBot File Manager बंद ===")
print("27va practical complete! Google ला पाठवायला तयार! 🚀")