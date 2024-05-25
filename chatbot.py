import nltk
from nltk.chat.util import Chat, reflections

# Sample pairs of patterns and responses
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how are you today?",]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there",]
    ],
    [
        r"what is your name ?",
        ["I am a chatbot created by you. You can call me Chatbot.",]
    ],
    [
        r"how are you ?",
        ["I'm doing good. How about you?",]
    ],
    [
        r"sorry",
        ["It's okay.", "No problem.",]
    ],
    [
        r"I am fine",
        ["Great to hear that! How can I assist you today?",]
    ],
    [
        r"thank you|thanks",
        ["You are always welcome:)."]
    ],
    [
        r"quit",
        ["Bye for now. See you soon!", "It was nice talking to you. Goodbye!"]
    ],
]

# Default reflections
reflections = {
    "i am"       : "you are",
    "i was"      : "you were",
    "i"          : "you",
    "i'd"        : "you would",
    "i've"       : "you have",
    "i'll"       : "you will",
    "my"         : "your",
    "you are"    : "I am",
    "you were"   : "I was",
    "you've"     : "I have",
    "you'll"     : "I will",
    "your"       : "my",
    "yours"      : "mine",
    "you"        : "me",
    "me"         : "you"
}

def chatbot():
    print("Hi! I'm your chatbot. Type 'quit' to exit.")
    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    chatbot()
