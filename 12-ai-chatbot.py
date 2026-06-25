print("Hello! I am an AI Chatbot! 🤖")
print("What is your name?")

name = input("Enter your name: ")
print(f"Wow {name}! How are you?")

while True:
    question = input(f"\n{name}, what should I do? ")
    
    if question.lower() == "bye":
        print("Bye Bye! See you again! 👋")
        break
    elif "how are you" in question.lower():
        print("I am great! How are you?")
    else:
        print(f"Hmm... I am still learning. Tell me more {name}!")