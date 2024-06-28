import tkinter as tk
from tkinter import messagebox
import random
import string
import ttkbootstrap as ttk

def password_generator(n, characters):
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation
    everything = letters + digits + symbols

    if characters == "letters":
        char_set = letters
    elif characters == "digits":
        char_set = digits
    elif characters == "symbols":
        char_set = symbols
    elif characters == "all":
        char_set = everything
    else:
        raise ValueError("Invalid character type specified. Use 'letters', 'digits', 'symbols', or 'all'.")

    password = ''.join(random.choice(char_set) for _ in range(n))
    return password

def generate_password():
    try:
        no_of_values = int(entry_length.get())
        if no_of_values <= 8:
            raise ValueError("The number of characters must be more then 8 characters for a stronger password.")
        
        character_type = character_type_var.get().lower()
        password = password_generator(no_of_values, character_type)
        entry_password.delete(0, tk.END)
        entry_password.insert(0, password)
    except ValueError as e:
        messagebox.showerror("Error", str(e))

def copy():
    copied_password = entry_password.get()
    if copied_password:
        root.clipboard_clear()
        root.clipboard_append(copied_password)
        messagebox.showinfo('copied!!!','Password has been successful copied to the clipboard!!!')
    else:
        messagebox.showerror('Error','No password was found')

# Creating the main window
root = ttk.Window(themename='simplex')
root.title("Password Generator")
root.geometry('800x400')

# Creating the widgets
ttk.Label(root, text="Number of characters:").place(x=50, y=50)
entry_length = ttk.Entry(root)
entry_length.place(x=200, y=50)

ttk.Label(root, text="Character type:").place(x=50, y=100)
character_type_var = ttk.StringVar()
ttk.OptionMenu(root, character_type_var, "all", "letters", "digits", "symbols", "all").place(x=200, y=100)

ttk.Button(root, text="Generate Password", command=generate_password).place(x=50, y=150)

ttk.Label(root, text="Generated Password:").place(x=50, y=200)
entry_password = ttk.Entry(root, width=50)
entry_password.place(x=200, y=200)

ttk.Button(root, text='📋', command=copy, bootstyle='white-outline').place(x=625, y=200)

# Start the Tkinter event loop
root.mainloop()
