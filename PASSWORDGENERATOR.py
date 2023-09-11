from tkinter import *
from tkinter import messagebox
import random
import string

root = Tk()
root.title("Random Password Generator")

def generate_random_password(length):
    upper_case = string.ascii_uppercase
    lower_case = string.ascii_lowercase
    digits = string.digits
    special_chars = string.punctuation

    characters = list(upper_case + lower_case + digits + special_chars)
    random.shuffle(characters)
    password = "".join(random.choices(characters, k=length))
    return password

def generate_password_length():
    try:
        password_length = int(entry_password_length.get())
        if password_length < 8:
            messagebox.showinfo("Error", "Password length must be at least 8 characters.")
            return

        generated_password = generate_random_password(password_length)
        label_generated_password.delete(0, END)
        label_generated_password.insert(0, generated_password)
    except ValueError:
        messagebox.showinfo("Error", "Please enter a valid integer for password length.")

label_username = Label(root, text="Username:")
label_username.grid(row=0, column=0, padx=10, pady=10)

label_password_length = Label(root, text="Password Length:")
label_password_length.grid(row=1, column=0, padx=10, pady=10)

entry_username = Entry(root)
entry_username.grid(row=0, column=1, padx=10, pady=10)

entry_password_length = Entry(root)
entry_password_length.grid(row=1, column=1, padx=10, pady=10)

generate_button = Button(root, text="Generate Password", command=generate_password_length)
generate_button.grid(row=2, column=1, padx=10, pady=10)

label_generated_password_text = Label(root, text="Generated Password:")
label_generated_password_text.grid(row=3, column=0, padx=10, pady=10)

label_generated_password = Entry(root)
label_generated_password.grid(row=3, column=1, padx=10, pady=10)

root.mainloop()
