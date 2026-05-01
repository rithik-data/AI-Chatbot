import json
import random
import nltk
from nltk.stem import WordNetLemmatizer

nltk.download('punkt')
nltk.download('wordnet')

lemmatizer = WordNetLemmatizer()

with open('intents.json') as file:
    data = json.load(file)

def clean_text(text):
    words = nltk.word_tokenize(text)
    words = [lemmatizer.lemmatize(word.lower()) for word in words]
    return words

def match_intent(user_input):
    user_words = clean_text(user_input)
    
    for intent in data['intents']:
        for pattern in intent['patterns']:
            pattern_words = clean_text(pattern)
            if any(word in user_words for word in pattern_words):
                return random.choice(intent['responses'])
    
    return "Sorry, I didn't understand that."

print("Chatbot running...")

while True:
    user_input = input("You: ")
    
    if user_input.lower() == 'exit':
        print("Bot: Goodbye!")
        break
    
    print("Bot:", match_intent(user_input))
