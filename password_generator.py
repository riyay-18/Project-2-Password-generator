import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password(length):
    all_characters = string.ascii_letters + string.digits + string.punctuation
    if length < 8:
        messagebox.showerror("Error", "Password length should be at least 8 characters.")
        return None
    password = ''.join(random.choice(all_characters) for i in range(length))
    return password

def main():
    root = tk.Tk()
    root.title("Password Generator")
    root.geometry("800x200")

    tk.Label(root, text="Password Length:").pack()
    length_entry = tk.Entry(root)
    length_entry.pack()

    def generate_and_display_password():
        length = int(length_entry.get())
        password = generate_password(length)
        if password:
            result_label.config(text=f"Generated Password: {password}")

    tk.Button(root, text="Generate Password", command=generate_and_display_password).pack()
    result_label = tk.Label(root, text="")
    result_label.pack()

    root.mainloop()

if __name__=="__main__":
    main()