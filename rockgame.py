import tkinter as tk
from tkinter import messagebox
import random

root = tk.Tk()
root.title("Rock Paper Scissors Game")
root.geometry("300x400")

user_score = 0
computer_score = 0

def play(choice):
    global user_score, computer_score

    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)

    if choice == computer_choice:
        result = "It's a Tie!"
    elif (choice == "rock" and computer_choice == "scissors") or \
         (choice == "paper" and computer_choice == "rock") or \
         (choice == "scissors" and computer_choice == "paper"):
        result = "You Win!"
        user_score += 1
    else:
        result = "You Lose!"
        computer_score += 1

    result_label.config(text=f"You: {choice}\nComputer: {computer_choice}\n{result}")
    score_label.config(text=f"Score\nYou: {user_score} | Computer: {computer_score}")

def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    result_label.config(text="")
    score_label.config(text="Score\nYou: 0 | Computer: 0")

# Buttons
tk.Label(root, text="Choose Rock, Paper, or Scissors", font=('Arial', 14)).pack(pady=10)

tk.Button(root, text="Rock", width=15, command=lambda: play("rock")).pack(pady=5)
tk.Button(root, text="Paper", width=15, command=lambda: play("paper")).pack(pady=5)
tk.Button(root, text="Scissors", width=15, command=lambda: play("scissors")).pack(pady=5)

result_label = tk.Label(root, text="", font=('Arial', 12))
result_label.pack(pady=20)

score_label = tk.Label(root, text="Score\nYou: 0 | Computer: 0", font=('Arial', 12))
score_label.pack()

tk.Button(root, text="Reset", command=reset_game).pack(pady=10)

root.mainloop()
