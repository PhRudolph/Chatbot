import json
import random

# Load intents from JSON files
def load_intents(file_path):
    with open(file_path, encoding='utf-8') as file:
        return json.load(file)

intents_english = load_intents('intends.json')
intents_german = load_intents('intents.json')

# Function to generate a random response from the intents database
def get_response(intent, language):
    intents = intents_english if language == 'en' else intents_german
    if intent in intents:
        responses = intents[intent]["responses"]
        return random.choice(responses)
    else:
        if language == 'en':
            return "I'm sorry, I couldn't understand your request. How can I assist you with your IT needs today?"
        else:
            return "Entschuldigung, ich konnte Ihre Anfrage nicht verstehen. Wie kann ich Ihnen heute mit Ihren IT-Anliegen helfen?"

# Main program loop
print("Welcome to the IT Service Chatbot!")
print("Please choose your preferred language: (1) English or (2) German")

language_choice = input("> ")
if language_choice == '1':
    language = 'en'
elif language_choice == '2':
    language = 'de'
else:
    print("Invalid choice. Exiting the chatbot.")
    exit()

intents = intents_english if language == 'en' else intents_german

if language == "en":
    print("How can I assist you with your IT needs today?")
else: print("Wie kann ich Ihnen Helfen?"),

while True:
    user_input = input("> ")

    if not user_input.strip():
        print("Exiting the chatbot.")
        break

    intent = ""

    for key, data in intents.items():
        patterns = data.get("patterns", [])
        if any(pattern in user_input.lower() for pattern in patterns):
            intent = key
            break

    response = get_response(intent, language)
    print(response)
