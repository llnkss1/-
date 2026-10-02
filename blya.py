import random
import tkinter as tk
from tkinter import messagebox

class Game:
    def __init__(self, root):
        self.root = root
        root.title("Угадай число")
        root.geometry("340x260")
        root.resizable(False, False)

        self.label = tk.Label(root, text="Я загадал число от 1 до 100", font=("Arial", 13))
        self.label.pack(pady=15)

        self.entry = tk.Entry(root, font=("Arial", 16), justify="center", width=8)
        self.entry.pack()
        self.entry.focus()
        self.entry.bind("<Return>", lambda e: self.check())

        tk.Button(root, text="Проверить", font=("Arial", 12), command=self.check).pack(pady=10)

        self.hint = tk.Label(root, text="", font=("Arial", 14))
        self.hint.pack(pady=5)

        self.counter = tk.Label(root, text="Попыток: 0", font=("Arial", 10))
        self.counter.pack()

        tk.Button(root, text="Заново", command=self.reset).pack(pady=8)

        self.reset()

    def reset(self):
        self.secret = random.randint(1, 100)
        self.attempts = 0
        self.hint.config(text="")
        self.counter.config(text="Попыток: 0")
        self.entry.delete(0, tk.END)

    def check(self):
        try:
            guess = int(self.entry.get())
        except ValueError:
            self.hint.config(text="Введи число!")
            return

        self.attempts += 1
        self.counter.config(text=f"Попыток: {self.attempts}")
        self.entry.delete(0, tk.END)

        if guess < self.secret:
            self.hint.config(text="Больше")
        elif guess > self.secret:
            self.hint.config(text="Меньше")
        else:
            messagebox.showinfo("Победа!", f"Угадал за {self.attempts} попыток!")
            self.reset()

root = tk.Tk()
Game(root)
root.mainloop()