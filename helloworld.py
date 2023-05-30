print("Hello I am a Chatbot. Type 'exit' to end program")

while True:
    anfrage = input(":")
    if anfrage == "exit":
        break
    else:
        print("echo: " + anfrage)

