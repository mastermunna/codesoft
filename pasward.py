import tkinter as tk
from tkinter import messagebox
import random
import string

# Generate password function
def generate_password():
    try:
        length = int(length_entry.get())
        if length <= 0:
            messagebox.showerror("Error", "Length must be greater than 0")
            return
        
        # Character set (uppercase, lowercase, digits, symbols)
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        
        result_entry.delete(0, tk.END)
        result_entry.insert(0, password)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number!")

# Copy password to clipboard
def copy_password():
    password = result_entry.get()
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")
    else:
        messagebox.showwarning("Warning", "No password to copy!")

# GUI Setup
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x300")
root.config(bg="#e8f5e9")

# Heading
tk.Label(root, text="🔐 Password Generator", font=("Arial", 20, "bold"), bg="#e8f5e9").pack(pady=10)

# Input field for length
tk.Label(root, text="Enter Password Length:", font=("Arial", 12), bg="#e8f5e9").pack()
length_entry = tk.Entry(root, font=("Arial", 12), width=10, justify="center")
length_entry.pack(pady=5)

# Generate button
tk.Button(root, text="Generate", font=("Arial", 12, "bold"), bg="#43a047", fg="white",
          command=generate_password).pack(pady=10)

# Result display
tk.Label(root, text="Generated Password:", font=("Arial", 12), bg="#e8f5e9").pack()
result_entry = tk.Entry(root, font=("Arial", 14), width=25, justify="center")
result_entry.pack(pady=5)

# Copy button
tk.Button(root, text="Copy to Clipboard", font=("Arial", 12, "bold"), bg="#1e88e5", fg="white",
          command=copy_password).pack(pady=10)

root.mainloop()
