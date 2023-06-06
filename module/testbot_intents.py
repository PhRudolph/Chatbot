import json
import random

# Load intents from JSON file
with open('intends.json') as file:
    intends = json.load(file)
with open('intents.json') as file:
    intents = json.load(file)

# Function to generate a random response from the intents database
def get_response(intent):
    if intent in intents:
        response = random.choice(intents[intent]["responses"])
        examples = intents[intent]["examples"]
        if examples:
            response += "\n\nHere are some example requests:\n" + "\n".join(examples)
        return response
    else:
        return "I'm sorry, I couldn't understand your request. How can I assist you with your IT needs today?"

# Main program loop
print("Welcome to the IT Service Desk Help Bot!")
print("How can I assist you with your IT needs today?")



while True:
    user_input = input("> ")
    response = get_response(user_input.lower())
    print(response)
