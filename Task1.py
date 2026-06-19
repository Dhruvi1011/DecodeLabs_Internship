#description to start

print("Welcome to RuleBot! I am a simple rule-based chatbot.")
print("Type 'menu' to see options.")
print("Type 'exit' to quit.")

#dict for response 
responses = {
    "hello": "Hi there!",
    "hi": "Hello!",
    "how are you": "I am fine, Thank you.",
    "what is your name": "I am RuleBot.",
    "Thank you": "You're welcome!",
    "thanks": "You're welcome!",
    " ": "I'm sorry, I didn't catch that.",
    "bye": "Goodbye!"
}

# AI Knowledge
ai_info = {
    "what is ai": "AI stands for Artificial Intelligence. It enables machines to perform tasks that normally require human intelligence.",
    
    "what is machine learning": "Machine Learning is a branch of AI that allows computers to learn patterns from data.",
    
    "what is deep learning": "Deep Learning is a subset of Machine Learning that uses neural networks with multiple layers."
}
 
 # loop
while True:

    user_input = input("You: ")
    clean_input = user_input.lower().strip()

    # Exit Command
    if clean_input == "exit":
        print("Bot: Chat ended. Goodbye!")
        break

    # Menu
    elif clean_input == "menu":
        print("""
===== MENU =====
General:
- hello
- hi
- how are you
- what is your name
- bye

AI Topics:
- what is ai
- what is machine learning
- what is deep learning

EXIT: Type 'exit' to quit

""")

    # AI Knowledge
    elif clean_input in ai_info:
        print("Bot:", ai_info[clean_input])

    # General Responses
    elif clean_input in responses:
        print("Bot:", responses[clean_input])

    # Unknown Input
    else:
        print("Bot: Sorry, I do not understand.")