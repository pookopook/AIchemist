import random
import tkinter as tk
choices = {
    "가위": "✌️",
    "바위": "✊",
    "보": "✋"
}

def play(user):
    computer = random.choice(list(choices.keys()))

    if user == computer:
        result = "비김"
    elif (user == "가위" and computer == "보") or \
         (user == "바위" and computer == "가위") or \
         (user == "보" and computer == "바위"):
        result = "승리"
    else:
        result = "패배"

    user_label.config(text=f"나: {choices[user]} {user}")
    computer_label.config(text=f"컴퓨터: {choices[computer]} {computer}")
    result_label.config(text=f"결과: {result}")

root = tk.Tk()
root.title("가위바위보 게임")
root.geometry("350x300")

title = tk.Label(root, text="가위바위보 게임", font=("Arial", 20))
title.pack(pady=15)

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

for name, icon in choices.items():
    btn = tk.Button(
        button_frame,
        text=f"{icon}\n{name}",
        font=("Arial", 18),
        width=6,
        height=3,
        command=lambda x=name: play(x)
    )
    btn.pack(side="left", padx=5)

user_label = tk.Label(root, text="나: ", font=("Arial", 14))
user_label.pack(pady=5)

computer_label = tk.Label(root, text="컴퓨터: ", font=("Arial", 14))
computer_label.pack(pady=5)

result_label = tk.Label(root, text="결과: ", font=("Arial", 18))
result_label.pack(pady=15)

root.mainloop()