# 21va Practical: String Operations - Palindrome Check
print("🔤 String Operations Practical")
print("="*35)

word = input("Ek shabd/number tak: ")

# Method 1: Reverse karun check
reverse_word = word[::-1] # [start:stop:step] -1 mhanje ulta

print(f"\nOriginal: {word}")
print(f"Reverse: {reverse_word}")

# Palindrome check
if word == reverse_word:
    print(f"✅ '{word}' ha Palindrome aahe!")
    print("Mhanje pudhe ani mage sarkhach vachto")
else:
    print(f"❌ '{word}' ha Palindrome nahi")

# Extra String operations
print("\n🔍 Extra String Info:")
print(f"1. Length: {len(word)} letters")
print(f"2. Uppercase: {word.upper()}")
print(f"3. Lowercase: {word.lower()}")
print(f"4. First letter: {word[0]}")
print(f"5. Last letter: {word[-1]}")

print("\nString practical complete! 🎉")