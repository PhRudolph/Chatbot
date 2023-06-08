#Startet den Chatbot und erwartet Input. Falls exit in den Chat geschrieben wird der Chatbot beendet
class chatbot():
    def run(self):
        print("Hello I am a Chatbot. Type 'exit' to end program")
        anfrage = input("")
        while anfrage != "exit":
            print("echo: " + anfrage)
            anfrage = input("")