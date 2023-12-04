import tkinter

window = tkinter.Tk()
window.title("Miles to Km Converter")
window.minsize(width=350, height=100)
window.config(padx=40, pady=20)

input = tkinter.Entry(width=10)
input.grid(column=1, row=0)

label_miles = tkinter.Label(text="Miles")
label_equal = tkinter.Label(text="is equal to")
label_convert = tkinter.Label(text="0")
label_km = tkinter.Label(text="Km")

label_miles.grid(column=2, row=0)
label_equal.grid(column=0, row=1)
label_convert.grid(column=1, row=1)
label_km.grid(column=2, row=1)

def miles_to_km():
    output = input.get()
    convert = round(float(output) * 1.609)
    label_convert.config(text=f"{convert}")

button = tkinter.Button(text="Calculate", command=miles_to_km)
button.grid(column=1, row=2)











window.mainloop()