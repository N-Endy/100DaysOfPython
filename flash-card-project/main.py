import tkinter
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

# ------------------ Generate Words --------------------

data = pandas.read_csv("./data/french_words.csv")
# word_list = data.to_dict(orient="records")
word_list = [{"French": row.French, "English": row.English} for (index, row) in data.iterrows()]

def next_card():
    word_choice = random.choice(word_list)
    canvas.itemconfig(title_text, text="French")
    canvas.itemconfig(word_text, text=word_choice["French"])


# ----------------- Window Ui ------------------------
window = tkinter.Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

'''
Create canvas, create photo image, load photo image and text on canvas. set to grid
'''
canvas = tkinter.Canvas(width=800, height=526)
card_front = tkinter.PhotoImage(file="./images/card_front.png")
canvas.create_image(400, 263, image=card_front)
title_text = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

wrong_button_img = tkinter.PhotoImage(file="./images/wrong.png")
wrong_button = tkinter.Button(image=wrong_button_img, highlightthickness=0, command=next_card)
right_button_img = tkinter.PhotoImage(file="./images/right.png")
right_button = tkinter.Button(image=right_button_img, highlightthickness=0, command=next_card)
wrong_button.grid(column=0, row=1)
right_button.grid(column=1, row=1)


next_card()







window.mainloop()