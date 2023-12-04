import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# Label
my_label = tkinter.Label(text="I Am a Label", font=("Arial", 24, "bold"))

my_label["text"] = "New Text"
my_label.config(text="New Text")
my_label.grid(column=0, row=0)

# Button
def button_click():
    output = input.get() 
    my_label["text"] = output

button = tkinter.Button(text="Click Me", command=button_click)
button1 = tkinter.Button(text="New Button")
button.grid(column=1, row=1)
button1.grid(column=2, row=0)

# Entry
input = tkinter.Entry(width=10)
input.grid(column=3, row=2)

# END = 0

# # Add some text to begin with
# entry = tkinter.Entry(width=30)
# entry.insert(END, string="Some text to begin with.")
# # Gets text in entry
# print(entry.get())
# entry.pack()

# # Text
# text = tkinter.Text(height=5, width=30)
# # Puts cursor in textbox
# text.focus()
# # Adds some text to begin with
# text.insert(END, "Example of multi-line text entry.")
# # Gets current value in textbox at line 1, character 0
# print(text.get("1.0"))
# text.pack()

# # Spinbox
# def spinbox_used():
#     # gets the current value in spinbox
#     print(spinbox.get())
# spinbox = tkinter.Spinbox(from_=0, to=10, width=5, command=spinbox_used)
# spinbox.pack()

# # Scale
# # called with current scale value
# def scale_used(value):
#     print(value)
# scale = tkinter.Scale(from_=0, to=100, command=scale_used)
# scale.pack()

# # Checkbutton
# def checkbutton_used():
#     # Prints 1 if On button checked, otherwise 0.
#     print(checked_state.get())
# # Variable to hold on to checked state, 0 is off, 1 is on
# checked_state = IntVar()
# checkedbutton = tkinter.Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)

# # Radiobutton
# def radio_used():
#     print(radio_state.get())
# # Variable to hold on to which radio button value is checked
# radio_state = IntVar()
# radiobutton1 = tkinter.Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
# radiobutton2 = tkinter.Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
# radiobutton1.pack()
# radiobutton2.pack()

# # Listbox
# def listbox_used(event):
#     # Gets current selection from listbox
#     print(listbox.get(listbox.curselection()))

# listbox = tkinter.Listbox(height=4)
# fruits = ["Apple", "Pear", "Orange", "Banana"]
# for item in fruits:
#     listbox.insert(fruits.index(item), item)
#     listbox.bind("<<ListboxSelect>>", listbox_used)
#     listbox.pack()




window.mainloop()