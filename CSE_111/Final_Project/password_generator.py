import tkinter as tk
import random as rand
from tkinter import Frame, Label, Button

def main():
    root = tk.Tk()
    frm_main = Frame(root)
    frm_main.master.title("Password Generator")
    frm_main.pack(padx=5, pady=5, fill=tk.BOTH, expand=1)
    populate_main_window(frm_main)
    root.mainloop()


def populate_main_window(frm_main):
    password_label = Label(frm_main, width=10, text='Password')
    password = Label(frm_main, width=50)
    var1 = tk.BooleanVar()
    c1 = tk.Checkbutton(frm_main, text='Letters', variable=var1, width=7)
    var2 = tk.BooleanVar()
    c2 = tk.Checkbutton(frm_main, text='Numbers', variable=var2, width=7)
    var3 = tk.BooleanVar()
    c3 = tk.Checkbutton(frm_main, text='Symbols', variable=var3, width=7)
    generate_button = Button(frm_main, text="Generate Password", command=lambda: generate_password(var1, var2, var3, password))
    password_label.grid(row=0, column=0, padx=5, pady=5)
    password.grid(row=0, column=1, padx=5, pady=5)
    c1.grid(row=1, column=0, padx=10, pady=10)
    c2.grid(row=1, column=1, padx=10, pady=10)
    c3.grid(row=1, column=2, padx=10, pady=10)
    generate_button.grid(row=2, columnspan=3, padx=10, pady=10)

def generate_password(var1, var2, var3, password):
    if var1.get() == True and var2.get() == False and var3.get() == False:
        password.config(text=letter_only_password())
    elif var1.get() == True and var2.get() == True and var3.get() == False:
        password.config(text=letters_and_numbers_password())
    elif var1.get() == False and var2.get() == True and var3.get() == False:
        password.config(text=number_only_password())
    elif var1.get() == True and var2.get() == True and var3.get() == True:
        password.config(text=letters_and_numbers_and_symbols_password())
    elif var1.get() == False and var2.get() == False and var3.get() == True:
        password.config(text=symbols_only_password())
    elif var1.get() == True and var2.get() == False and var3.get() == True:
        password.config(text=letters_and_symbols_password())
    elif var1.get() == False and var2.get() == True and var3.get() == True:
        password.config(text=numbers_and_symbols_password())
    else:
        password.config(text='You must check at least one box to generate a password.')


def letter_only_password():
    chars = 'abcdefghijklmnopqrstuvwxyz'
    password = ''
    for c in range(16):
        password += rand.choice(chars)
    return password

def letters_and_numbers_password():
    chars = 'abcdefghijklmnopqrstuvwxyz1234567890'
    password = ''
    for c in range(16):
        password += rand.choice(chars)
    return password

def letters_and_numbers_and_symbols_password():
    chars = 'abcdefghijklmnopqrstuvwxyz1234567890`~!@#$%^&*()-_=+[{]}|;:"\',<.>/?]'
    password = ''
    for c in range(16):
        password += rand.choice(chars)
    return password

def letters_and_symbols_password():
    chars = 'abcdefghijklmnopqrstuvwxyz`~!@#$%^&*()-_=+[{]}|;:"\',<.>/?]'
    password = ''
    for c in range(16):
        password += rand.choice(chars)
    return password

def numbers_and_symbols_password():
    chars = '1234567890`~!@#$%^&*()-_=+[{]}|;:"\',<.>/?]'
    password = ''
    for c in range(16):
        password += rand.choice(chars)
    return password

def number_only_password():
    chars = '1234567890'
    password = ''
    for c in range(16):
        password += rand.choice(chars)
    return password

def symbols_only_password():
    chars = '`~!@#$%^&*()-_=+[{]}|;:"\',<.>/?]'
    password = ''
    for c in range(16):
        password += rand.choice(chars)
    return password


if __name__ == "__main__":
    main()