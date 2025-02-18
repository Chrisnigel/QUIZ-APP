import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from ttkthemes import ThemedTk

# Define the quiz questions
questions = [
    {
        "question": "What is 2 + 2?",
        "options": ["3", "4", "5", "6"],
        "answer": "4"
    },
    {
        "question": "What is the capital of France?",
        "options": ["Berlin", "Madrid", "Paris", "Rome"],
        "answer": "Paris"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Earth", "Mars", "Jupiter", "Venus"],
        "answer": "Mars"
    },
    {
        "question": "Who developed the theory of relativity?",
        "options": ["Isaac Newton", "Albert Einstein", "Nikola Tesla", "Galileo Galilei"],
        "answer": "Albert Einstein"
    },
    {
        "question": "Which is the smallest country in the world?",
        "options": ["Monaco", "Vatican City", "San Marino", "Liechtenstein"],
        "answer": "Vatican City"
    }
]

# Initialize the window
window = ThemedTk(theme="arc")  # Using the "arc" theme from ttkthemes
window.title("Python Quiz App")
window.geometry("600x500")

# Variables to track the current question and score
current_question_index = 0
score = 0

# Function to load the current question
def load_question():
    global current_question_index
    question = questions[current_question_index]
    
    # Clear previous question
    for widget in frame_question.winfo_children():
        widget.destroy()

    # Display current question
    question_label = ttk.Label(frame_question, text=question["question"], font=("Arial", 14))
    question_label.pack(pady=10)

    # Display options as radio buttons
    for option in question["options"]:
        option_var = tk.StringVar()
        radio_button = ttk.Radiobutton(frame_question, text=option, value=option, variable=option_var)
        radio_button.pack(anchor="w", padx=20)

    # Next button
    next_button = ttk.Button(frame_question, text="Next", command=next_question)
    next_button.pack(pady=20)

# Function to check the answer and move to the next question
def next_question():
    global current_question_index, score
    
    selected_option = None
    for widget in frame_question.winfo_children():
        if isinstance(widget, ttk.Radiobutton):
            if widget.instate(['selected']):
                selected_option = widget.cget("text")

    if selected_option:
        correct_answer = questions[current_question_index]["answer"]
        if selected_option == correct_answer:
            score += 1

    current_question_index += 1

    if current_question_index < len(questions):
        load_question()
    else:
        show_result()

# Function to display the result
def show_result():
    result_message = f"You scored {score} out of {len(questions)}!"
    messagebox.showinfo("Quiz Finished", result_message)
    window.quit()

# Frame to hold the question and options
frame_question = ttk.Frame(window)
frame_question.pack(pady=20)

# Load the first question
load_question()

# Run the GUI application
window.mainloop()
