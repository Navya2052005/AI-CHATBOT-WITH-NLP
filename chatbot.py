import nltk
import random
import string

# Download required resources
nltk.download('punkt')
nltk.download('wordnet')

from nltk.chat.util import Chat, reflections

# Define pairs (patterns and responses)
pairs = [
    [r"hi|hello|hey", ["Hello! How can I help you today?", "Hi there!"]],
    [r"what is your name?", ["I am an AI chatbot built with Python.", "You can call me PyBot!"]],
    [r"how are you?", ["I'm doing great! How about you?", "I'm fine, thanks for asking."]],
    [r"what is NLP?", ["NLP stands for Natural Language Processing. It's how computers understand human language."]],
    [r"(.) your favourite (.)", ["I don't have favorites, but I like learning new things!"]],
    [r"quit", ["Bye! Have a great day."]]
]

# Create chatbot
chatbot = Chat(pairs, reflections)

# Start conversation
print("Hi! I'm your AI Chatbot. Type 'quit' to exit.")
chatbot.converse()