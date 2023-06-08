import unittest
from unittest.mock import patch
from io import StringIO

from chatbot import chatbot

#Test für den Chatbot
class ChatBotTests(unittest.TestCase):
    def test_chatbot_exit(self):
        with patch('builtins.input', side_effect=["exit"]):
            with patch('sys.stdout', new=StringIO()) as output:
                chatbot.run(self)
                self.assertEqual("Hello I am a Chatbot. Type 'exit' to end program\n", output.getvalue())

    def test_chatbot_echo(self):
        with patch('builtins.input', side_effect=["Hello", "How are you?", "exit"]):
            with patch('sys.stdout', new=StringIO()) as output:
                chatbot.run(self)
                self.assertIn("echo: Hello", output.getvalue())
                self.assertIn("echo: How are you?", output.getvalue())
                
unittest.main()
