import random

# Define patterns for user inputs and their corresponding response options
patterns = {
    "greetings": {
        "patterns": ["hello", "hi", "hey"],
        "responses": ["Hello! How can I assist you with your IT needs today?", "Hi there! How can I help you?", "Hey! How can I assist you with your IT issues?"],
    },
    "password_reset": {
        "patterns": ["forgot password", "reset password", "password help"],
        "responses": ["To reset your password, please contact our IT support team at support@company.com or call our helpline at 123-456-7890."],
    },
    "software_installation": {
        "patterns": ["software installation", "install software", "need software"],
        "responses": ["To request software installation, please submit a ticket through our online help desk portal or contact the IT support team for further assistance."],
    },
    "hardware_issue": {
        "patterns": ["hardware problem", "hardware issue", "device not working"],
        "responses": ["For hardware issues, please submit a ticket with a detailed description of the problem. Our IT support team will promptly assist you."],
    },
    "network_troubleshooting": {
        "patterns": ["network problem", "connectivity issue", "internet not working"],
        "responses": ["To troubleshoot network connectivity issues, please ensure that you are connected to the correct network, restart your device, and contact the IT support team if the problem persists."],
    },
    "default": {
        "patterns": ["default"],
        "responses": ["I'm sorry, I couldn't understand your request. How can I assist you with your IT needs today?"],
    },
}

# Define keywords and their corresponding intent
keywords = {
    "greetings": ["hello", "hi", "hey"],
    "password_reset": ["password"],
    "software_installation": ["software"],
    "hardware_issue": ["hardware"],
    "network_troubleshooting": ["network", "connectivity", "internet"],
}

# Function to match user input with patterns
def match_pattern(user_input):
    for intent, data in patterns.items():
        for pattern in data["patterns"]:
            if pattern in user_input:
                return intent
    return "default"

# Function to generate a random response from the response options
def get_response(intent):
    if intent in patterns:
        return random.choice(patterns[intent]["responses"])
    else:
        return random.choice(patterns["default"]["responses"])

# Main program loop
print("Welcome to the IT Service Chatbot!")
print("How can I assist you with your IT needs today?")

while True:
    user_input = input("> ")
    user_input = user_input.lower()

    intent = match_pattern(user_input)
    response = get_response(intent)

    print(response)
