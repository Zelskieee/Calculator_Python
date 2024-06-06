import tkinter as tk
from tkinter import messagebox
import re

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Magical Calculator")
        self.previous = 0

        self.equation = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        # Entry widget for input and display
        entry = tk.Entry(self.root, textvariable=self.equation, font=("Arial", 20), bd=10, insertwidth=4, width=14, borderwidth=4)
        entry.grid(row=0, column=0, columnspan=4)

        # Buttons
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('+', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('-', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('*', 3, 3),
            ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('/', 4, 3),
        ]

        for (text, row, col) in buttons:
            button = tk.Button(self.root, text=text, padx=20, pady=20, font=("Arial", 18),
                               command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, sticky="nsew")

        # Adjust column and row configurations
        for i in range(4):
            self.root.grid_columnconfigure(i, weight=1)
        for i in range(5):
            self.root.grid_rowconfigure(i, weight=1)

    def on_button_click(self, char):
        if char == 'C':
            self.equation.set("")
            self.previous = 0
        elif char == '=':
            self.calculate()
        else:
            current_text = self.equation.get()
            new_text = current_text + char
            self.equation.set(new_text)

    def calculate(self):
        equation = self.equation.get()
        equation = re.sub('[a-zA-Z,. :()"]', '', equation)
        try:
            if self.previous == 0:
                self.previous = eval(equation)
            else:
                self.previous = eval(str(self.previous) + equation)
            self.equation.set(str(self.previous))
        except Exception as e:
            messagebox.showerror("Error", "Invalid input. Please enter a valid equation.")
            self.equation.set("")
            self.previous = 0

if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()
