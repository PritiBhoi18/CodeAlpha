#basic chatbot
import time
now = time.ctime()

QnA = {
    "Hii":"Hello",
    "How are you?":"I am Great",
    "What is your name?":"My name is Basic Chatbot",
    "Where are you from?":"I am from your python program.",
    "What is your age?":"I am 20 years old.",
    "What is the time now?":now,
}

while True:
    qs = input()

    if(qs== "quit"):
        break
    
    else:
        print(QnA[qs])
