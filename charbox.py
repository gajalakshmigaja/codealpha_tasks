def get_response(message):
    message = message.lower().strip()

    if message in ["hello", "hi", "hii", "hey", "hai"]:
        return "Hi!"

    elif message in ["how are you", "how r u", "how are u"]:
        return "I'm fine, thanks! How about you?"

    elif message in ["good morning", "gm"]:
        return "Good Morning! 😊"

    elif message in ["good afternoon", "ga"]:
        return "Good Afternoon! 😊"

    elif message in ["good night", ""]:
        return "Good Evening! 😊"

    elif message in ["thanks", "thank you", "thx"]:
        return "You're welcome! 😊"

    elif message in ["bye", "goodbye", "see you"]:
        return "Goodbye! Have a nice day!"

    else:
        return "Sorry, I don't understand. Can you say it differently?"

while True:
    user = input("You: ")

    response = get_response(user)
    print("Bot:", response)

    if user.lower().strip() in ["bye", "goodbye", "see you"]:
        break