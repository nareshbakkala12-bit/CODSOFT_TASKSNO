# CODSOFT_TASKSNO
CODSOFT AI Internship Tasks
print("🤖 Welcome to Simple AI Chatbot!")
print("Type 'bye' to exit.")

while True:
    user_input = input("You: ").lower().strip()

    if user_input in ["hello", "hi", "hey"]:
        print("Bot: Hello! How can I help you?")

    elif "your name" in user_input or "who are you" in user_input:
        print("Bot: I am a simple AI chatbot created using Python.")

    elif "how are you" in user_input:
        print("Bot: I'm doing great! Thanks for asking.")

    elif "help" in user_input:
        print("Bot: Sure! I can answer some basic questions.")

    elif "thank" in user_input:
        print("Bot: You're welcome!")

    elif "bye" in user_input or "exit" in user_input:
        print("Bot: Goodbye! Have a nice day!")
        break

    else:
        print("Bot: Sorry, I don't understand that.")
