import tkinter
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

# ------------------ Generate Words --------------------

try:
    data = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("./data/french_words.csv")
finally:
    # word_list = data.to_dict(orient="records")
    word_list = [{"French": row.French, "English": row.English} for (index, row) in data.iterrows()]

def next_card():
    global flip_timer
    window.after_cancel(flip_timer)
    word_choice = random.choice(word_list)
    canvas.itemconfig(title_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=word_choice["French"], fill="black")
    canvas.itemconfig(canvas_image, image=card_front)
    flip_timer = window.after(3000, func=flip_card)
    return word_choice
    
    
def flip_card():
    english_word = next_card()
    canvas.itemconfig(title_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=english_word["English"], fill="white")
    canvas.itemconfig(canvas_image, image=card_back)
    
    
def is_known():
    word_list.remove(next_card())
    data = pandas.DataFrame(word_list)
    data.to_csv("./data/words_to_learn.csv", index=False)
    next_card()


# ----------------- Window Ui ------------------------
window = tkinter.Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)


'''
Create canvas, create photo image, load photo image and text on canvas. set to grid
'''
canvas = tkinter.Canvas(width=800, height=526)
card_front = tkinter.PhotoImage(file="./images/card_front.png")
card_back = tkinter.PhotoImage(file="./images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=card_front)
title_text = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

wrong_button_img = tkinter.PhotoImage(file="./images/wrong.png")
wrong_button = tkinter.Button(image=wrong_button_img, highlightthickness=0, command=next_card)
right_button_img = tkinter.PhotoImage(file="./images/right.png")
right_button = tkinter.Button(image=right_button_img, highlightthickness=0, command=is_known)
wrong_button.grid(column=0, row=1)
right_button.grid(column=1, row=1)


next_card()







window.mainloop()