import tkinter

BACKGROUND_COLOR = "#B1DDC6"

# ----------------- WIndow Ui ------------------------
window = tkinter.Tk()
window.title("Flashy")

'''
Create canvas, create photo image, load photo image and text on canvas. set to grid
'''
canvas = tkinter.Canvas(width=800, height=526)
card_front = tkinter.PhotoImage(file="./images/card_front.png")
canvas.create_image(400, 263, image=card_front)
language_text = canvas.create_text(400, 150, text="French", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text="trouve", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

wrong_button_img = tkinter.PhotoImage(file="./images/wrong.png")
wrong_button = tkinter.Button(image=wrong_button_img, highlightthickness=0, padx=50)
right_button_img = tkinter.PhotoImage(file="./images/right.png")
right_button = tkinter.Button(image=right_button_img, highlightthickness=0, padx=50)
wrong_button.grid(column=0, row=1)
right_button.grid(column=1, row=1)










window.mainloop()