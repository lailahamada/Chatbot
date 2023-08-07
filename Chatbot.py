import tkinter as tk


qa_pairs = [
    ("Hello", "Hi"),
    ("How are you?", "I'm just a tour guide chatbot, I have no feelings"),
    ("What's your name?", "I'm a chatbot."),
    ("What is AI?", "AI stands for Artificial Intelligence. It refers to the simulation of human intelligence in machines."),
    ("What are the applications of AI?", "AI has various applications, such as natural language processing, computer vision, robotics, and data analysis."),
    ("How does AI impact our daily lives?", "AI has a significant impact on our daily lives, from voice assistants like Siri and Alexa to personalized recommendations on streaming platforms."),
    ("What are some examples of AI in use today?", "Some examples of AI in use today include self-driving cars, virtual personal assistants, and fraud detection systems.")
]


def get_response():
    user_input = entry.get()
    display_text = f"You: {user_input}\n"
    chat_text.insert(tk.END, display_text)
    entry.delete(0, tk.END)

    for question, response in qa_pairs:
        if user_input.lower() in question.lower():
            chat_text.insert(tk.END, f"Chatbot: {response}\n\n")
            return

    
    chat_text.insert(tk.END, "Chatbot: I'm sorry, I don't have a specific response to that question.\n\n")


window = tk.Tk()
window.title("AI Chatbot")


chat_text = tk.Text(window, width=50, height=20)
chat_text.pack()


entry_label = tk.Label(window, text="You:")
entry_label.pack()
entry = tk.Entry(window, width=50)
entry.pack()


submit_button = tk.Button(window, text="Submit", command=get_response)
submit_button.pack()


window.mainloop()
