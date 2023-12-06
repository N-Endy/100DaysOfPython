import tkinter
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

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
website.grid(column=0, row=1)
website_input.grid(column=1, row=1, columnspan=2)

email = tkinter.Label(text="Email/Usrename:")
email_input = tkinter.Entry(width=42)
email.grid(column=0, row=2)
email_input.grid(column=1, row=2, columnspan=2,)

password = tkinter.Label(text="Password:")
password_input = tkinter.Entry(width=24)
generate_password = tkinter.Button(text="Generate Password", width=14)
password.grid(column=0, row=3)
password_input.grid(column=1, row=3)
generate_password.grid(column=2, row=3)

add_button = tkinter.Button(text="Add", width=40)
add_button.grid(column=1, row=4, columnspan=2)

















window.mainloop()