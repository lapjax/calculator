import tkinter as tk

def update_input(value):
    current = str(entry.get())
    entry.delete(0, tk.END)
    entry.insert(0, current + value)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def clear():
    entry.delete(0, tk.END)

root = tk.Tk()
root.title("Calculator")

entry = tk.Entry(root, width = 35, borderwidth = 5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2),
    ('0', 4, 1), ('+', 1, 3), ('-', 2, 3),
    ('*', 3, 3), ('/', 4, 3), ('=', 4, 2),
    ('C', 4, 0)
]

for text, row, col in buttons:
    button = tk.Button(root, text=text, padx=20, pady=20, command=lambda t=text: update_input(t) if t not in {'=', 'C'} else (calculate() if t == '=' else clear()))
    button.grid(row=row, column=col, sticky="nsew")

root.mainloop()