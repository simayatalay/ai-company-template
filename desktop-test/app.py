import tkinter as tk


def greet():
    name = name_entry.get()
    result_label.config(text=f"Hello, {name}! Welcome to the project.")


root = tk.Tk()
root.title("Desktop Test Demo")

name_entry = tk.Entry(root)
name_entry.pack(padx=20, pady=10)

greet_button = tk.Button(root, text="Greet", command=greet)
greet_button.pack(padx=20, pady=10)

result_label = tk.Label(root, text="")
result_label.pack(padx=20, pady=10)

root.mainloop()