from random import choice, randint, shuffle
import tkinter
from tkinter import messagebox
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)
        
    final_password = "".join(password_list)
        

    password_input.delete(0, 'end')
    password_input.insert(0, final_password)
    
    # Copy the password to clip
    pyperclip.copy(final_password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
'''
Saves website name, email, and password to new file before deleting entries in input fields
'''
def save():
    website_entry = website_input.get()
    email_entry = email_input.get()
    password_entry = password_input.get()
    
    if len(website_entry) == 0 or len(password_entry) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website_entry, message=f"These are the entries entered: \nEmail: {email_entry} \nPassword: {password_entry} \nIs it okay to save?")
        
        with open("./data_file.txt", "a") as data_file:
            data_file.write(f"{website_entry} | {email_entry} | {password_entry}\n")
        
        website_input.delete(0, 'end')
        password_input.delete(0, 'end')


# ---------------------------- UI SETUP ------------------------------- #
# Window setup
window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Canvas and Image
canvas = tkinter.Canvas(width=200, height=200, highlightthickness=0)
photo_img = tkinter.PhotoImage(file="./logo.png")
canvas.create_image(100, 100, image=photo_img)
canvas.grid(column=1, row=0)

# Labels, Inputs and Buttons
website = tkinter.Label(text="Website:")
website_input = tkinter.Entry(width=42)
website_input.focus()
website.grid(column=0, row=1)
website_input.grid(column=1, row=1, columnspan=2)

email = tkinter.Label(text="Email/Username:")
email_input = tkinter.Entry(width=42)
email_input.insert(0, "okafornel@gmail.com")
email.grid(column=0, row=2)
email_input.grid(column=1, row=2, columnspan=2,)

password = tkinter.Label(text="Password:")
password_input = tkinter.Entry(width=24)
generate_password = tkinter.Button(text="Generate Password", width=14, command=gen_password)
password.grid(column=0, row=3)
password_input.grid(column=1, row=3)
generate_password.grid(column=2, row=3)

add_button = tkinter.Button(text="Add", width=40, command=save)
add_button.grid(column=1, row=4, columnspan=2)

















window.mainloop()