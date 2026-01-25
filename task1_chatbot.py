def chatbot():
    print("🤖 Chatbot: Hello! I am a rule-based chatbot.")
    print("Type 'bye' to exit.\n")

    while True:
        user_input = input("You: ").lower()

        if user_input == "bye":
            print("🤖 Chatbot: Goodbye! Have a nice day 😊")
            break

        elif "hello" in user_input or "hi" in user_input:
            print("🤖 Chatbot: Hello! How can I help you?")

        elif "how are you" in user_input:
            print("🤖 Chatbot: I'm doing great! Thanks for asking.")

        elif "your name" in user_input:
            print("🤖 Chatbot: I am a simple rule-based chatbot.")

        elif "help" in user_input:
            print("🤖 Chatbot: I can answer simple questions like greetings, name, and status.")

        elif "thank you" in user_input or "thanks" in user_input:
            print("🤖 Chatbot: You're welcome! 😊")

        else:
            print("🤖 Chatbot: Sorry, I didn't understand that.")

chatbot()
