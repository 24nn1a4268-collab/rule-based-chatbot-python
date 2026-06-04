import tkinter as tk
from tkinter import scrolledtext

# Function to generate chatbot responses
def chatbot_response(user_input):
    user_input = user_input.lower()

    responses = {
        "hello": "Hi! How can I help you?",
        "hi": "Hello! Nice to meet you.",
        "how are you": "I am fine. Thank you!",
        "what is your name": "I am a Rule-Based Chatbot.",
        "bye": "Goodbye! Have a great day!",
        "help": "You can ask me simple questions."
    }

    for key in responses:
        if key in user_input:
            return responses[key]

    return "Sorry, I don't understand that."

# Function to send message
def send_message():
    user_message = entry.get()

    if user_message.strip() != "":
        chat_area.insert(tk.END, "You: " + user_message + "\n")

        bot_reply = chatbot_response(user_message)

        chat_area.insert(tk.END, "Bot: " + bot_reply + "\n\n")

        entry.delete(0, tk.END)

# Create GUI Window
window = tk.Tk()
window.title("Rule-Based Chatbot")
window.geometry("500x500")

# Chat display area
chat_area = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=60, height=20)
chat_area.pack(pady=10)

# User input box
entry = tk.Entry(window, width=40)
entry.pack(side=tk.LEFT, padx=10, pady=10)

# Send button
send_button = tk.Button(window, text="Send", command=send_message)
send_button.pack(side=tk.LEFT)

# Run application
window.mainloop()