import tkinter as tk
from tkinter import messagebox

# Function to update expression in the input field
def click(button_text):
    current = str(entry.get())
    if button_text == "=":
        try:
            result = eval(current)
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except ZeroDivisionError:
            messagebox.showerror("Error", "Division by zero is not allowed!")
        except:
            messagebox.showerror("Error", "Invalid Expression!")
    elif button_text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, button_text)

# Main window setup
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x400")
root.config(bg="#e3f2fd")

# Entry field for displaying expressions
entry = tk.Entry(root, font=("Arial", 20), borderwidth=5, relief="ridge", justify="right")
entry.pack(pady=20, padx=10, fill=tk.X)

# Button layout
buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', 'C', '+'],
    ['=']
]

# Frame for buttons
frame = tk.Frame(root, bg="#e3f2fd")
frame.pack()

# Create buttons dynamically
for row in buttons:
    row_frame = tk.Frame(frame, bg="#e3f2fd")
    row_frame.pack(expand=True, fill='both')
    for btn_text in row:
        tk.Button(
            row_frame, text=btn_text, font=("Arial", 18), bg="#90caf9", fg="black",
            relief="raised", command=lambda t=btn_text: click(t)
        ).pack(side="left", expand=True, fill="both", padx=2, pady=2)

root.mainloop()
