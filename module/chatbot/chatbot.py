class chatbot():
    def run(self):
        print("Hello I am a Chatbot. Type 'exit' to end program")
        anfrage = input("")
        while anfrage != "exit":
            print("echo: " + anfrage)
            anfrage = input("")