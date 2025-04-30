import nltk
import random
from nltk.chat.util import Chat, reflections

# Define pairs of patterns and responses
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today?",]
    ],
    [
        r"what is your name?",
        ["My name is Chatbot and I'm here to help you.",]
    ],
    [
        r"how are you ?",
        ["I'm doing good\nHow about You ?",]
    ],
    [
        r"sorry (.*)",
        ["It's alright", "It's OK, never mind",]
    ],
    [
        r"i'm (.*) doing good",
        ["Nice to hear that", "Alright :)",]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there",]
    ],
    [
        r"(.*) age?",
        ["I'm a computer program \n Age is just a number",]
    ],
    [
        r"what (.*) want ?",
        ["Make me an offer I can't refuse",]
    ],
    [
        r"(.*) created ?",
        ["Rahul Jadahv created me using Python's NLTK library ", "top secret ;)",]
    ],
    [
        r"(.*) (location|city) ?",
        ['Nashik, India',]
    ],
    [
        r"how is weather in (.*)?",
        ["Weather in %1 is awesome like always", "Too hot man here in %1", "Too cold man here in %1", "Never even heard about %1"]
    ],
    [
        r"i work in (.*)?",
        ["%1 is an Amazing company, I have heard about it. But they are in huge loss these days.",]
    ],
    [
        r"(.*)raining in (.*)",
        ["No rain since last week here in %2", "Damn its raining too much here in %2"]
    ],
    [
        r"how (.*) health(.*)",
        ["I'm a computer program, so I'm always healthy ",]
    ],
    [
        r"(.*) (sports|game) ?",
        ["I'm a very big fan of Cricket",]
    ],
    [
        r"who (.*) (Cricketer|Batsman)?",
        ["Virat Kohli"]
    ],
    [
        r"customer service",
        ["For customer service, please call our helpline at +1-800-123-4567."]
    ],
    [
        r"contact number|phone number",
        ["Our customer service contact number is +1-800-123-4567."]
    ],
    [
        r"quit",
        ["Bye take care. See you soon :) ", "It was nice talking to you. See you soon :)"]
    ],
]

# Create a chatbot
chatbot = Chat(pairs, reflections)

def main():
    print("Welcome to the NLTK Chatbot!")
    print("Type 'quit' to end the conversation.")

    while True:
        user_input = input("You: ")
        response = chatbot.respond(user_input)
        print("Chatbot:", response)

        if user_input.lower() == "quit":
            break

if __name__ == "__main__":
    main()
