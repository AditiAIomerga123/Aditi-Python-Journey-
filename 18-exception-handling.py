# 18va Practical: Exception Handling
print("🛡️ Error Handling Practical")
print("="*35)

# Problem: User chukicha input deil tar program crash hoto
# Solution: try/except vaprun error handle kar

try:
    num1 = int(input("Pahila number tak: "))
    num2 = int(input("Dusra number tak: "))
    
    result = num1 / num2
    print(f"\nResult: {num1} / {num2} = {result}")

except ZeroDivisionError:
    print("\n❌ Error: 0 ne bhagta yet nahi!")
    
except ValueError:
    print("\n❌ Error: Fakt number tak! Shabd nako!")

except Exception as e:
    print(f"\n❌ Kahi tari error aali: {e}")

else:
    print("✅ Calculation yashasvi zala!")
    
finally:
    print("\nProgram complete zala. Thank you! 🙏")