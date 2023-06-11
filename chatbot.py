def greet():
    print("Hello! How can I assist you today?")

def chatbot_response(user_input):
    user_input = user_input.lower()
    
    if "hello" in user_input or "hi" in user_input:
        return "Hi"
    elif "how are you" in user_input:
        return "I'm good. How about you?"
    elif "great" in user_input:
        return "That's great to hear!"
    elif "weather" in user_input:
        return "Today weather is 35 degree"
    elif "goodbye" in user_input:
        return "Goodbye! Thank you, Have a nice day."
    else:
        return "I'm sorry, I didn't understand. Could you please ask a different question?"

def chat():
    greet()
    
    while True:
        user_input = input("User: ")
        
        if user_input.lower() == "exit":
            break
        
        response = chatbot_response(user_input)
        print("ChatBot:", response)

chat()
