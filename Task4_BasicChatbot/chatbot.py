def get_reply(message):
    """Return a predefined reply for the user's message."""
    message = message.lower().strip()

    if message in ["hello", "hi", "hey"]:
        return "Hi! Nice to meet you."
    elif message == "how are you":
        return "I'm fine, thanks! How about you?"
    elif message in ["i'm fine", "im fine", "i am fine", "good"]:
        return "Glad to hear that!"
    elif message in ["what is your name", "your name"]:
        return "I'm CodeBot, a simple rule-based chatbot."
    elif message in ["what can you do", "help"]:
        return "I can say hello, ask how you are, and say goodbye. Try 'hello', 'how are you' or 'bye'."
    elif message in ["thanks", "thank you"]:
        return "You're welcome!"
    elif message in ["bye", "goodbye", "exit"]:
        return "Goodbye!"
    else:
        return "Sorry, I don't understand that. Type 'help' to see what I can do."


def main():
    print("CodeBot: Hello! I'm CodeBot. Type 'bye' to end the chat.")

    while True:
        user_input = input("You: ")
        reply = get_reply(user_input)
        print("CodeBot:", reply)

        if reply == "Goodbye!":
            break


main()
