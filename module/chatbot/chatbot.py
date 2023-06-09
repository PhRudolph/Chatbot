import json
import random
import sys

sys.path.append('module/')

from database.database import database
from mail_service.mail_service import mail_service

# Load intents from JSON files
def load_intents(file_path):
    with open(file_path, encoding='utf-8') as file:
        return json.load(file)

intents_english = load_intents('intents.json')
intents_german = load_intents('intends.json')

# Function to generate a random response from the intents database
def get_response(user_input, intent, language):
    intents = intents_english if language == 'en' else intents_german
    if intent in intents:
        responses = intents[intent]["responses"]
        return random.choice(responses)
    else:
        db = database()
        mailservice = mail_service()
        
        db.connectToDb("database.db")
        
        create_sql = "".join("CREATE TABLE errorRequests(requestId INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, requestText TEXT NOT NULL)") 
        print(create_sql)
        db.executeStatement(create_sql)
        
        insert_sql = "".join("INSERT INTO errorRequests (requestText) VALUES ("+ user_input + ");")
        print(insert_sql)
        db.executeStatement(insert_sql)
        
        mailservice.mail_service("FEHLER BEI CHATBOT ", user_input)
        
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
        if language == "en": 
            print("Exiting the chatbot."),
            
        else:    
            print("Chatbot wird deaktiviert."),
        break

    intent = ""

    for key, data in intents.items():
        examples = data.get("examples", [])
        for example in examples:
            if (example.lower() in user_input.lower()):
                intent = key
                break

    response = get_response(user_input, intent, language)
    print(response)
